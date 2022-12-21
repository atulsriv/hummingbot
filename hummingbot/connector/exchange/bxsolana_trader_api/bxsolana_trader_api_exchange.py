from abc import ABC
from decimal import Decimal
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

from hummingbot.connector.constants import s_decimal_NaN
from hummingbot.connector.exchange.bitmart.bitmart_auth import BitmartAuth
from hummingbot.connector.exchange_py_base import ExchangePyBase
from hummingbot.connector.trading_rule import TradingRule
from hummingbot.core.data_type.common import OrderType, TradeType
from hummingbot.core.data_type.in_flight_order import InFlightOrder, OrderUpdate, TradeUpdate
from hummingbot.core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
from hummingbot.core.data_type.trade_fee import AddedToCostTradeFee
from hummingbot.core.data_type.user_stream_tracker_data_source import UserStreamTrackerDataSource
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory

if TYPE_CHECKING:
    from hummingbot.client.config.config_helpers import ClientConfigAdapter


class BloxRouteTraderAPI(ExchangePyBase, ABC):
    """
    BloxRouteTraderAPI connects with bloxRoute Labs Inc. Solana Trader AP exchange and provides order book pricing, user account tracking and
    trading functionality.

    See more at bloXRoute Labs documentation: https://docs.bloxroute.com/bloxroute-solana-trading-suite/api/trade-api

    # TODO: Add more comment about bloXroute Labs and Solana Trader API here

    """
    API_CALL_TIMEOUT = 10.0
    POLL_INTERVAL = 1.0
    UPDATE_ORDER_STATUS_MIN_INTERVAL = 10.0
    UPDATE_TRADE_STATUS_MIN_INTERVAL = 10.0

    def __init__(self,
                 client_config_map: "ClientConfigAdapter",
                 auth_header: str,
                 trading_pairs: Optional[List[str]] = None,
                 trading_required: bool = True,
                 ):
        """
        :param auth_header: The authorization header to connect to bloXroute Labs Solana-Trader-API
        :param trading_pairs: The market trading pairs which to track order book data.
        :param trading_required: Whether actual trading is needed.
        """

        self._api_key: str = ""
        self._trading_required = trading_required
        self._trading_pairs = trading_pairs

        super().__init__(client_config_map)
        self.real_time_balance_update = False

    @property
    def authenticator(self):
        return BitmartAuth(
            api_key=self._api_key,
            time_provider=self._time_synchronizer)

    @property
    def name(self) -> str:
        return "bitmart"

    @property
    def rate_limits_rules(self):
        pass

    @property
    def domain(self):
        pass

    @property
    def client_order_id_max_length(self):
        pass

    @property
    def client_order_id_prefix(self):
        pass

    @property
    def trading_rules_request_path(self):
        pass

    @property
    def trading_pairs_request_path(self):
        pass

    @property
    def check_network_request_path(self):
        pass

    @property
    def trading_pairs(self):
        pass

    @property
    def is_cancel_request_in_exchange_synchronous(self) -> bool:
        return True

    @property
    def is_trading_required(self) -> bool:
        return self._trading_required

    def supported_order_types(self) -> List[OrderType]:
        """
        :return a list of OrderType supported by this connector.
        Note that Market order type is no longer required and will not be used.
        """
        raise "Not implemented yet!"

    def _is_request_exception_related_to_time_synchronizer(self, request_exception: Exception):
        raise "Not implemented yet!"

    def _create_web_assistants_factory(self) -> WebAssistantsFactory:
        raise "Not implemented yet!"

    def _create_order_book_data_source(self) -> OrderBookTrackerDataSource:
        raise "Not implemented yet!"

    def _create_user_stream_data_source(self) -> UserStreamTrackerDataSource:
        raise "Not implemented yet!"

    def _get_fee(self,
                 base_currency: str,
                 quote_currency: str,
                 order_type: OrderType,
                 order_side: TradeType,
                 amount: Decimal,
                 price: Decimal = s_decimal_NaN,
                 is_maker: Optional[bool] = None) -> AddedToCostTradeFee:
        """
        To get trading fee, this function is simplified by using fee override configuration. Most parameters to this
        function are ignore except order_type. Use OrderType.LIMIT_MAKER to specify you want trading fee for
        maker order.
        """
        raise "Not implemented yet!"

    async def _place_order(self,
                           order_id: str,
                           trading_pair: str,
                           amount: Decimal,
                           trade_type: TradeType,
                           order_type: OrderType,
                           price: Decimal,
                           **kwargs) -> Tuple[str, float]:

        raise "Not implemented yet!"

    async def _place_cancel(self, order_id: str, tracked_order: InFlightOrder):
        raise "Not implemented yet!"

    async def _format_trading_rules(self, symbols_details: Dict[str, Any]) -> List[TradingRule]:
        raise "Not implemented yet!"

    async def _update_trading_fees(self):
        """
        Update fees information from the exchange
        """
        pass

    async def _update_balances(self):
        raise "Not implemented yet!"

    async def _request_order_update(self, order: InFlightOrder) -> Dict[str, Any]:
        raise "Not implemented yet!"

    async def _request_order_fills(self, order: InFlightOrder) -> Dict[str, Any]:
        raise "Not implemented yet!"

    async def _all_trade_updates_for_order(self, order: InFlightOrder) -> List[TradeUpdate]:
        raise "Not implemented yet!"

    async def _request_order_status(self, tracked_order: InFlightOrder) -> OrderUpdate:
        raise "Not implemented yet!"

    def _create_order_fill_updates(self, order: InFlightOrder, fill_update: Dict[str, Any]) -> List[TradeUpdate]:
        raise "Not implemented yet!"

    def _create_order_update(self, order: InFlightOrder, order_update: Dict[str, Any]) -> OrderUpdate:
        raise "Not implemented yet!"

    async def _user_stream_event_listener(self):
        raise "Not implemented yet!"

    def _initialize_trading_pair_symbols_from_exchange_info(self, exchange_info: Dict[str, Any]):
        raise "Not implemented yet!"

    async def _get_last_traded_price(self, trading_pair: str) -> float:
        raise "Not implemented yet!"
