---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sap-abap_1_iot-data-plane_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS IoT data examples using SDK for SAP ABAP
<a name="sap-abap_1_iot-data-plane_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with AWS IoT data.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetThingShadow`
<a name="iot-data-plane_GetThingShadow_sap-abap_1_topic"></a>

The following code example shows how to use `GetThingShadow`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/iop#code-examples).

```
    TRY.
        DATA(lo_result) = lo_iop->getthingshadow( iv_thingname = iv_thing_name ).

        " Convert xstring payload to JSON string
        DATA(lv_payload) = lo_result->get_payload( ).
        ov_shadow = /aws1/cl_rt_util=>xstring_to_string( lv_payload ).
        MESSAGE 'Thing shadow retrieved successfully.' TYPE 'I'.
      CATCH /aws1/cx_iopresourcenotfoundex.
        MESSAGE 'Thing shadow not found.' TYPE 'E'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_exception).
        DATA(lv_error) = |{ lo_exception->get_text( ) }|.
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [GetThingShadow](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `UpdateThingShadow`
<a name="iot-data-plane_UpdateThingShadow_sap-abap_1_topic"></a>

The following code example shows how to use `UpdateThingShadow`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/iop#code-examples).

```
    TRY.
        " Convert JSON string to xstring for payload
        DATA(lv_payload) = /aws1/cl_rt_util=>string_to_xstring( iv_shadow_state ).

        lo_iop->updatethingshadow(
          iv_thingname = iv_thing_name
          iv_payload = lv_payload ).
        MESSAGE 'Thing shadow updated successfully.' TYPE 'I'.
      CATCH /aws1/cx_iopresourcenotfoundex.
        MESSAGE 'Thing not found.' TYPE 'E'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_exception).
        DATA(lv_error) = |{ lo_exception->get_text( ) }|.
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [UpdateThingShadow](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
