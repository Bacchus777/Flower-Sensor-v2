from typing import Final
import logging

from zigpy.quirks import CustomCluster
from zigpy.quirks.v2 import EntityType, QuirkBuilder, ReportingConfig
from zigpy.quirks.v2.homeassistant import UnitOfTime#, PERCENTAGE
from zigpy.quirks.v2.homeassistant.number import NumberDeviceClass
from zigpy.quirks.v2.homeassistant.sensor import SensorDeviceClass
import zigpy.types as t
from zigpy.zcl.clusters.general import (
    Time
)
from zigpy.zcl.clusters.measurement import (
    SoilMoisture
)
from zigpy.zcl.foundation import ZCLAttributeDef

_LOGGER = logging.getLogger(__name__)

class BWSoilMoisture(CustomCluster, SoilMoisture):
    """Bacchus Soil Moisture cluster."""

    cluster_id = 0x0408
    class AttributeDefs(SoilMoisture.AttributeDefs):
        """Bacchus Soil Moisture cluster attributes."""

        # This attribute specifies the demand of a switched load when it is energised
        bw_report_delay: Final = ZCLAttributeDef(
            id = 0x0203,
            type = t.uint16_t,
            access = "rw",
        )

        bw_threshold: Final = ZCLAttributeDef(
            id = 0x0202,
            type = t.uint16_t,
            access = "rw",
        )

(
    QuirkBuilder("Bacchus", "Flower_Sensor_v2")
    .replaces(BWSoilMoisture, endpoint_id = 1)
    .number(
        cluster_id = BWSoilMoisture.cluster_id,
        endpoint_id = 1,
        attribute_name = BWSoilMoisture.AttributeDefs.bw_report_delay.name,
        translation_key = "report_delay",
        fallback_name = "Report delay",
        device_class = NumberDeviceClass.DURATION,
        unit = UnitOfTime.MINUTES,
        min_value = 0,
        max_value = 600,
        step = 1,
    )
    .number(
        cluster_id = BWSoilMoisture.cluster_id,
        endpoint_id = 1,
        attribute_name = BWSoilMoisture.AttributeDefs.bw_threshold.name,
        translation_key = "threshold",
        fallback_name = "Threshold",
        device_class = NumberDeviceClass.MOISTURE,
        step = 1,
        min_value = 0,
        max_value = 100,
        )
    .add_to_registry()
)