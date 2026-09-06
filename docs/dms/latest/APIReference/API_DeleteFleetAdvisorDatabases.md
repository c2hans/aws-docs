---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteFleetAdvisorDatabases.html
---

# DeleteFleetAdvisorDatabases
<a name="API_DeleteFleetAdvisorDatabases"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Deletes the specified Fleet Advisor collector databases.

## Request Syntax
<a name="API_DeleteFleetAdvisorDatabases_RequestSyntax"></a>

```
{
   "DatabaseIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteFleetAdvisorDatabases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseIds](#API_DeleteFleetAdvisorDatabases_RequestSyntax) **   <a name="DMS-DeleteFleetAdvisorDatabases-request-DatabaseIds"></a>
The IDs of the Fleet Advisor collector databases to delete.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_DeleteFleetAdvisorDatabases_ResponseSyntax"></a>

```
{
   "DatabaseIds": [ "string" ]
}
```

## Response Elements
<a name="API_DeleteFleetAdvisorDatabases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatabaseIds](#API_DeleteFleetAdvisorDatabases_ResponseSyntax) **   <a name="DMS-DeleteFleetAdvisorDatabases-response-DatabaseIds"></a>
The IDs of the databases that the operation deleted.
Type: Array of strings

## Errors
<a name="API_DeleteFleetAdvisorDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidOperationFault **
The action or operation requested isn't valid.
HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DeleteFleetAdvisorDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteFleetAdvisorDatabases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteFleetAdvisorDatabases)
