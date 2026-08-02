---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_PutCapacityAssignmentConfiguration.html
---

# PutCapacityAssignmentConfiguration
<a name="API_PutCapacityAssignmentConfiguration"></a>

Puts a new capacity assignment configuration for a specified capacity reservation. If a capacity assignment configuration already exists for the capacity reservation, replaces the existing capacity assignment configuration.

## Request Syntax
<a name="API_PutCapacityAssignmentConfiguration_RequestSyntax"></a>

```
{
   "CapacityAssignments": [
      {
         "WorkGroupNames": [ "{{string}}" ]
      }
   ],
   "CapacityReservationName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutCapacityAssignmentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CapacityAssignments](#API_PutCapacityAssignmentConfiguration_RequestSyntax) **   <a name="athena-PutCapacityAssignmentConfiguration-request-CapacityAssignments"></a>
The list of assignments for the capacity assignment configuration.
Type: Array of [CapacityAssignment](API_CapacityAssignment.md) objects
Required: Yes

 ** [CapacityReservationName](#API_PutCapacityAssignmentConfiguration_RequestSyntax) **   <a name="athena-PutCapacityAssignmentConfiguration-request-CapacityReservationName"></a>
The name of the capacity reservation to put a capacity assignment configuration for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

## Response Elements
<a name="API_PutCapacityAssignmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutCapacityAssignmentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

## See Also
<a name="API_PutCapacityAssignmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/PutCapacityAssignmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/PutCapacityAssignmentConfiguration)
