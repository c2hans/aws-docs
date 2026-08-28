---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_UpdateRestrictedExecutionTimes.html
---

# UpdateRestrictedExecutionTimes
<a name="API_UpdateRestrictedExecutionTimes"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

Replaces the existing times when change execution is restricted.

## Request Syntax
<a name="API_UpdateRestrictedExecutionTimes_RequestSyntax"></a>

```
{
   "RestrictedExecutionTimes": [
      {
         "TimeRange": {
            "EndTime": "{{string}}",
            "StartTime": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateRestrictedExecutionTimes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RestrictedExecutionTimes](#API_UpdateRestrictedExecutionTimes_RequestSyntax) **   <a name="amscm-UpdateRestrictedExecutionTimes-request-RestrictedExecutionTimes"></a>
The new restricted time ranges.
Type: Array of [RestrictedExecutionTime](API_RestrictedExecutionTime.md) objects
Required: Yes

## Response Elements
<a name="API_UpdateRestrictedExecutionTimes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRestrictedExecutionTimes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An unspecified server error occurred.
HTTP Status Code: 500

 ** InvalidArgumentException **
A specified argument is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRestrictedExecutionTimes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amscm-2020-05-21/UpdateRestrictedExecutionTimes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/UpdateRestrictedExecutionTimes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
