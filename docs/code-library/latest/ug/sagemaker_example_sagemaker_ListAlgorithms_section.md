---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sagemaker_example_sagemaker_ListAlgorithms_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListAlgorithms` with an AWS SDK
<a name="sagemaker_example_sagemaker_ListAlgorithms_section"></a>

The following code example shows how to use `ListAlgorithms`.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sgm#code-examples).

```
    TRY.
        oo_result = lo_sgm->listalgorithms(         " oo_result is returned for testing purposes. "
          iv_namecontains = iv_name_contains ).
        MESSAGE 'Retrieved list of algorithms.' TYPE 'I'.
      CATCH /aws1/cx_rt_service_generic INTO DATA(lo_exception).
        DATA(lv_error) = |"{ lo_exception->av_err_code }" - { lo_exception->av_err_msg }|.
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListAlgorithms](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------
