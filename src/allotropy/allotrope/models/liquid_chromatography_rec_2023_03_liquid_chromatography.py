# generated by datamodel-codegen:
#   filename:  liquid-chromatography.json
#   timestamp: 2024-05-23T13:20:45+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCentimeter,
    TQuantityValueCubicMillimeter,
    TQuantityValueHertz,
    TQuantityValueMicrometer,
    TQuantityValueMillimeter,
    TQuantityValueNanometer,
    TQuantityValuePercent,
    TQuantityValueSecondTime,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDatacube,
    TDateTimeValue,
    TQuantityValue,
    TStringValue,
)


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    pump_model_number: TStringValue | None = None
    detector_model_number: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None


@dataclass(kw_only=True)
class ChromatographyColumnDocument:
    chromatography_column_particle_size: TQuantityValueMicrometer | None = None
    chromatography_column_chemistry_type: TStringValue | None = None
    chromatography_column_serial_number: TStringValue | None = None
    column_inner_diameter: TQuantityValueMillimeter | None = None
    product_manufacturer: TStringValue | None = None
    chromatography_column_length: TQuantityValueCentimeter | None = None
    chromatography_column_part_number: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    model_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    detection_type: TStringValue | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = (
        None
    )
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = (
        None
    )
    detector_offset_setting: TQuantityValue | None = None
    detector_sampling_rate_setting: TQuantityValueHertz | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    written_name: TStringValue | None = None


@dataclass(kw_only=True)
class InjectionDocument:
    autosampler_injection_volume_setting__chromatography_: TQuantityValueCubicMillimeter
    injection_identifier: TStringValue
    injection_time: TDateTimeValue


@dataclass(kw_only=True)
class PeakItem:
    retention_time: TQuantityValueSecondTime
    peak_end: TQuantityValueSecondTime | None = None
    identifier: TStringValue | None = None
    relative_peak_height: TQuantityValuePercent | None = None
    written_name: TStringValue | None = None
    peak_height: TQuantityValue | None = None
    capacity_factor__chromatography_: TQuantityValueUnitless | None = None
    peak_area: TQuantityValue | None = None
    relative_peak_area: TQuantityValuePercent | None = None
    peak_start: TQuantityValueSecondTime | None = None
    peak_selectivity__chromatography_: TQuantityValueUnitless | None = None
    peak_width_at_4_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_13_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_32_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_60_7___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_half_height: TQuantityValueSecondTime | None = None
    peak_width_at_5___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_baseline: TQuantityValueSecondTime | None = None
    peak_width_at_inflection: TQuantityValueSecondTime | None = None
    peak_width_at_10___of_height: TQuantityValueSecondTime | None = None
    peak_width: TQuantityValueSecondTime | None = None
    statistical_skew__chromatography_: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_5___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_10___height: TQuantityValueUnitless | None = None
    asymmetry_factor_squared_measured_at_10___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_squared_measured_at_4_4___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_measured_at_4_4___height: TQuantityValueUnitless | None = None
    chromatographic_peak_asymmetry_factor: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_baseline: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_baseline_peak_widths: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_statistical_moments: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates__chromatography_: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_60_7___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_32_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_13_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_4_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_tangent_method: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_by_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height__JP14_: TQuantityValueUnitless | None = (
        None
    )
    field_index: int | None = None


@dataclass(kw_only=True)
class PeakList:
    peak: list[PeakItem] | None = None


@dataclass(kw_only=True)
class ProcessedDataDocument:
    peak_list: PeakList | None = None


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any
    data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None


@dataclass(kw_only=True)
class MeasurementDocumentItem:
    chromatography_column_document: ChromatographyColumnDocument
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    injection_document: InjectionDocument
    detection_type: TStringValue
    chromatogram_data_cube: TDatacube
    measurement_identifier: TStringValue | None = None
    three_dimensional_ultraviolet_spectrum_data_cube: TDatacube | None = None
    processed_data_document: ProcessedDataDocument | None = None
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocumentItem]


@dataclass(kw_only=True)
class LiquidChromatographyDocumentItem:
    analyst: TStringValue
    measurement_aggregate_document: MeasurementAggregateDocument
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class LiquidChromatographyAggregateDocument:
    device_system_document: DeviceSystemDocument
    liquid_chromatography_document: list[LiquidChromatographyDocumentItem]


@dataclass(kw_only=True)
class Model:
    manifest: str = "http://purl.allotrope.org/manifests/liquid-chromatography/REC/2023/03/liquid-chromatography.manifest"
    liquid_chromatography_aggregate_document: LiquidChromatographyAggregateDocument | None = (
        None
    )
