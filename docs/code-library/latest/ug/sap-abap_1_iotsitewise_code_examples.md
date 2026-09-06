---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sap-abap_1_iotsitewise_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS IoT SiteWise examples using SDK for SAP ABAP
<a name="sap-abap_1_iotsitewise_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with AWS IoT SiteWise.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello AWS IoT SiteWise
<a name="iotsitewise_Hello_sap-abap_1_topic"></a>

The following code example shows how to get started using AWS IoT SiteWise.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->listassetmodels( ). " oo_result is returned for testing purposes. "
        DATA(lt_asset_models) = oo_result->get_assetmodelsummaries( ).
        MESSAGE 'Retrieved list of asset models.' TYPE 'I'.
      CATCH /aws1/cx_rt_generic.
        MESSAGE 'Unable to list asset models.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListAssetModels](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

## Actions
<a name="actions"></a>

### `BatchPutAssetPropertyValue`
<a name="iotsitewise_BatchPutAssetPropertyValue_sap-abap_1_topic"></a>

The following code example shows how to use `BatchPutAssetPropertyValue`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        lo_ios->batchputassetpropertyvalue(
          it_entries = it_entries
        ).
        MESSAGE 'Data sent to IoT SiteWise asset successfully.' TYPE 'I'.
      CATCH /aws1/cx_iosresourcenotfoundex.
        MESSAGE 'Asset does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateAsset`
<a name="iotsitewise_CreateAsset_sap-abap_1_topic"></a>

The following code example shows how to use `CreateAsset`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->createasset(
          iv_assetname = iv_asset_name
          iv_assetmodelid = iv_asset_model_id
        ). " oo_result is returned for testing purposes. "
        MESSAGE 'IoT SiteWise asset created' TYPE 'I'.
      CATCH /aws1/cx_iosresourcenotfoundex.
        MESSAGE 'Asset model does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateAsset](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateAssetModel`
<a name="iotsitewise_CreateAssetModel_sap-abap_1_topic"></a>

The following code example shows how to use `CreateAssetModel`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->createassetmodel(
          iv_assetmodelname = iv_asset_model_name
          iv_assetmodeldescription = 'This is a sample asset model description.'
          it_assetmodelproperties = it_properties
        ). " oo_result is returned for testing purposes. "
        MESSAGE 'IoT SiteWise asset model created' TYPE 'I'.
      CATCH /aws1/cx_iosresrcalrdyexistsex.
        MESSAGE 'Asset model already exists.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateAssetModel](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateGateway`
<a name="iotsitewise_CreateGateway_sap-abap_1_topic"></a>

The following code example shows how to use `CreateGateway`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->creategateway(
          iv_gatewayname = iv_gateway_name
          io_gatewayplatform = NEW /aws1/cl_iosgatewayplatform(
            io_greengrassv2 = NEW /aws1/cl_iosgreengrassv2(
              iv_coredevicethingname = iv_core_device_thing_name
            )
          )
          it_tags = VALUE /aws1/cl_iostagmap_w=>tt_tagmap(
            (
              VALUE /aws1/cl_iostagmap_w=>ts_tagmap_maprow(
                key = 'Environment'
                value = NEW /aws1/cl_iostagmap_w( 'Production' )
              )
            )
          )
        ). " oo_result is returned for testing purposes. "
        MESSAGE 'IoT SiteWise gateway created' TYPE 'I'.
      CATCH /aws1/cx_iosresrcalrdyexistsex.
        MESSAGE 'Gateway already exists.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateGateway](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteAsset`
<a name="iotsitewise_DeleteAsset_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteAsset`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        lo_ios->deleteasset(
          iv_assetid = iv_asset_id
        ).
        MESSAGE 'IoT SiteWise asset deleted.' TYPE 'I'.
      CATCH /aws1/cx_rt_generic.
        MESSAGE 'Unable to delete asset.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteAsset](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteAssetModel`
<a name="iotsitewise_DeleteAssetModel_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteAssetModel`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        lo_ios->deleteassetmodel(
          iv_assetmodelid = iv_asset_model_id
        ).
        MESSAGE 'IoT SiteWise asset model deleted.' TYPE 'I'.
      CATCH /aws1/cx_rt_generic.
        MESSAGE 'Unable to delete asset model.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteAssetModel](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteGateway`
<a name="iotsitewise_DeleteGateway_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteGateway`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        lo_ios->deletegateway(
          iv_gatewayid = iv_gateway_id
        ).
        MESSAGE 'IoT SiteWise gateway deleted.' TYPE 'I'.
      CATCH /aws1/cx_iosresourcenotfoundex.
        MESSAGE 'Gateway does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteGateway](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeGateway`
<a name="iotsitewise_DescribeGateway_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeGateway`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->describegateway(
          iv_gatewayid = iv_gateway_id
        ). " oo_result is returned for testing purposes. "
        MESSAGE 'Retrieved gateway description.' TYPE 'I'.
      CATCH /aws1/cx_iosresourcenotfoundex.
        MESSAGE 'Gateway does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeGateway](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `GetAssetPropertyValue`
<a name="iotsitewise_GetAssetPropertyValue_sap-abap_1_topic"></a>

The following code example shows how to use `GetAssetPropertyValue`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->getassetpropertyvalue(
          iv_assetid = iv_asset_id
          iv_propertyid = iv_property_id
        ). " oo_result is returned for testing purposes. "
        MESSAGE 'Retrieved asset property value.' TYPE 'I'.
      CATCH /aws1/cx_iosresourcenotfoundex.
        MESSAGE 'Asset or property does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [GetAssetPropertyValue](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListAssetModelProperties`
<a name="iotsitewise_ListAssetModelProperties_sap-abap_1_topic"></a>

The following code example shows how to use `ListAssetModelProperties`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->listassetmodelproperties(
          iv_assetmodelid = iv_asset_model_id
        ). " oo_result is returned for testing purposes. "
        DATA(lt_properties) = oo_result->get_assetmodelpropertysums( ).
        MESSAGE 'Retrieved list of asset model properties.' TYPE 'I'.
      CATCH /aws1/cx_rt_generic.
        MESSAGE 'Unable to list asset model properties.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListAssetModelProperties](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListAssetModels`
<a name="iotsitewise_ListAssetModels_sap-abap_1_topic"></a>

The following code example shows how to use `ListAssetModels`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ios#code-examples).

```
    TRY.
        oo_result = lo_ios->listassetmodels( ). " oo_result is returned for testing purposes. "
        DATA(lt_asset_models) = oo_result->get_assetmodelsummaries( ).
        MESSAGE 'Retrieved list of asset models.' TYPE 'I'.
      CATCH /aws1/cx_rt_generic.
        MESSAGE 'Unable to list asset models.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListAssetModels](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
