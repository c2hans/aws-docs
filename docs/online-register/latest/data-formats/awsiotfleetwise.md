---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awsiotfleetwise.html
---

# Data retrieval APIs for AWS IoT FleetWise
<a name="awsiotfleetwise"></a>

AWS IoT FleetWise provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="iotfleetwise-GetCampaign"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetCampaign.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetCampaign.html) | Get summary information for a given campaign | Read |
| <a name="iotfleetwise-GetDecoderManifest"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetDecoderManifest.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetDecoderManifest.html) | Get summary information for a given decoder manifest definition | Read |
| <a name="iotfleetwise-GetEncryptionConfiguration"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetEncryptionConfiguration.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetEncryptionConfiguration.html) | Get KMS-based encryption status for the AWS account | Read |
| <a name="iotfleetwise-GetFleet"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetFleet.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetFleet.html) | Get summary information for a fleet | Read |
| <a name="iotfleetwise-GetLoggingOptions"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetLoggingOptions.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetLoggingOptions.html) | Get the logging options for the AWS account | Read |
| <a name="iotfleetwise-GetModelManifest"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetModelManifest.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetModelManifest.html) | Get summary information for a given model manifest definition | Read |
| <a name="iotfleetwise-GetRegisterAccountStatus"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetRegisterAccountStatus.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetRegisterAccountStatus.html) | Get the account registration status with IoT FleetWise | Read |
| <a name="iotfleetwise-GetSignalCatalog"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetSignalCatalog.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetSignalCatalog.html) | Get summary information for a specific signal catalog | Read |
| <a name="iotfleetwise-GetStateTemplate"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetStateTemplate.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetStateTemplate.html) | Get summary information for a given state template | Read |
| <a name="iotfleetwise-GetVehicle"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicle.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicle.html) | Get summary information for a vehicle | Read |
| <a name="iotfleetwise-GetVehicleStatus"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicleStatus.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetVehicleStatus.html) | Get the status of the campaigns running on a specific vehicle | Read |
| <a name="iotfleetwise-ListCampaigns"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListCampaigns.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListCampaigns.html) | List campaigns | Read |
| <a name="iotfleetwise-ListDecoderManifestNetworkInterfaces"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestNetworkInterfaces.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestNetworkInterfaces.html) | List network interfaces associated to the existing decoder manifest | List |
| <a name="iotfleetwise-ListDecoderManifestSignals"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestSignals.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestSignals.html) | List decoder manifest signals | List |
| <a name="iotfleetwise-ListDecoderManifests"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifests.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifests.html) | List all decoder manifests, with an optional filter on model manifest | Read |
| <a name="iotfleetwise-ListFleets"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleets.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleets.html) | List all fleets | Read |
| <a name="iotfleetwise-ListFleetsForVehicle"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleetsForVehicle.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListFleetsForVehicle.html) | List all the fleets that the given vehicle is associated with | Read |
| <a name="iotfleetwise-ListModelManifestNodes"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifestNodes.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifestNodes.html) | List all nodes for the given model manifest | List |
| <a name="iotfleetwise-ListModelManifests"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifests.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListModelManifests.html) | List all model manifests, with an optional filter on signal catalog | Read |
| <a name="iotfleetwise-ListSignalCatalogNodes"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogNodes.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogNodes.html) | List all nodes for a given signal catalog | Read |
| <a name="iotfleetwise-ListSignalCatalogs"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogs.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListSignalCatalogs.html) | List all signal catalogs | Read |
| <a name="iotfleetwise-ListStateTemplates"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListStateTemplates.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListStateTemplates.html) | List state templates | Read |
| <a name="iotfleetwise-ListTagsForResource"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListTagsForResource.html) | List tags for a resource | Read |
| <a name="iotfleetwise-ListVehicles"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehicles.html) | List all vehicles, with an optional filter on model manifest | Read |
| <a name="iotfleetwise-ListVehiclesInFleet"></a>[https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehiclesInFleet.html](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListVehiclesInFleet.html) | List vehicles in the given fleet | Read |
