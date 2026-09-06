---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/sap-abap_bedrock-runtime_code_examples.html
---

# Amazon Bedrock Runtime examples using SDK for SAP ABAP
<a name="sap-abap_bedrock-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Amazon Bedrock Runtime.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Stable Image Core](#stable_image_core)

## Stable Image Core
<a name="stable_image_core"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_StableDiffusion_sap-abap_topic"></a>

The following code example shows how to invoke Stability.ai Stable Image Core on Amazon Bedrock to generate an image.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/bdr#code-examples).
Create an image with Stable Diffusion.

```
    "Stable Image Core Input Parameters should be in a format like this:
*   {
*     "prompt": "Draw a dolphin with a mustache, photorealistic",
*     "aspect_ratio": "1:1",
*     "seed": 0,
*     "output_format": "png"
*   }
    DATA: BEGIN OF ls_input,
            prompt        TYPE /aws1/rt_shape_string,
            aspect_ratio  TYPE /aws1/rt_shape_string,
            seed          TYPE /aws1/rt_shape_integer,
            output_format TYPE /aws1/rt_shape_string,
          END OF ls_input.

    ls_input-prompt = iv_prompt.
    ls_input-aspect_ratio = '1:1'.
    ls_input-seed = 0. "or better, choose a random integer.
    ls_input-output_format = 'png'.

    DATA(lv_json) = /ui2/cl_json=>serialize(
      data = ls_input
                pretty_name   = /ui2/cl_json=>pretty_mode-low_case ).

    TRY.
        DATA(lo_response) = lo_bdr->invokemodel(
          iv_body = /aws1/cl_rt_util=>string_to_xstring( lv_json )
          iv_modelid = 'stability.stable-image-core-v1:1'
          iv_accept = 'application/json'
          iv_contenttype = 'application/json' ).

        "Stable Image Core Result Format:
*       {
*         "seeds": ["0"],
*         "finish_reasons": [null],
*         "images": ["iVBORw0KGgoAAAANSUhEUgAAAgAAA...."]
*       }
        DATA: BEGIN OF ls_response,
                images TYPE STANDARD TABLE OF /aws1/rt_shape_string,
              END OF ls_response.

        /ui2/cl_json=>deserialize(
          EXPORTING jsonx = lo_response->get_body( )
                    pretty_name = /ui2/cl_json=>pretty_mode-camel_case
          CHANGING  data  = ls_response ).
        IF ls_response-images IS NOT INITIAL.
          DATA(lv_image) = cl_http_utility=>if_http_utility~decode_x_base64( ls_response-images[ 1 ] ).
        ENDIF.
      CATCH /aws1/cx_bdraccessdeniedex INTO DATA(lo_ex).
        WRITE / lo_ex->get_text( ).
        WRITE / |Don't forget to enable model access at https://console.aws.amazon.com/bedrock/home?#/modelaccess|.

    ENDTRY.
```
Invoke the Stability.ai Stable Image Core foundation model to generate images using L2 high level client.

```
    TRY.
        DATA(lo_bdr_l2_sd) = /aws1/cl_bdr_l2_factory=>create_stable_diffusion_xl_1( lo_bdr ).
        " iv_prompt contains a prompt like 'Show me a picture of a unicorn reading an enterprise financial report'.
        DATA(lv_image) = lo_bdr_l2_sd->text_to_image( iv_prompt ).
      CATCH /aws1/cx_bdraccessdeniedex INTO DATA(lo_ex).
        WRITE / lo_ex->get_text( ).
        WRITE / |Don't forget to enable model access at https://console.aws.amazon.com/bedrock/home?#/modelaccess|.

    ENDTRY.
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
