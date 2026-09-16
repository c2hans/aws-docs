---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_BatchStartRecommendations.html
---

# BatchStartRecommendations
<a name="API_BatchStartRecommendations"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Starts the analysis of up to 20 source databases to recommend target engines for each source database. This is a batch version of [StartRecommendations](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartRecommendations.html).

The result of analysis of each source database is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of `200`.

## Request Syntax
<a name="API_BatchStartRecommendations_RequestSyntax"></a>

```
{
   "Data": [
      {
         "DatabaseId": "{{string}}",
         "Settings": {
            "InstanceSizingType": "{{string}}",
            "WorkloadType": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_BatchStartRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Data](#API_BatchStartRecommendations_RequestSyntax) **   <a name="DMS-BatchStartRecommendations-request-Data"></a>
Provides information about source databases to analyze. After this analysis, Fleet Advisor recommends target engines for each source database.
Type: Array of [StartRecommendationsRequestEntry](API_StartRecommendationsRequestEntry.md) objects
Required: No

## Response Syntax
<a name="API_BatchStartRecommendations_ResponseSyntax"></a>

```
{
   "ErrorEntries": [
      {
         "Code": "string",
         "DatabaseId": "string",
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchStartRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ErrorEntries](#API_BatchStartRecommendations_ResponseSyntax) **   <a name="DMS-BatchStartRecommendations-response-ErrorEntries"></a>
A list with error details about the analysis of each source database.
Type: Array of [BatchStartRecommendationsErrorEntry](API_BatchStartRecommendationsErrorEntry.md) objects

## Errors
<a name="API_BatchStartRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_BatchStartRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/BatchStartRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/BatchStartRecommendations)
