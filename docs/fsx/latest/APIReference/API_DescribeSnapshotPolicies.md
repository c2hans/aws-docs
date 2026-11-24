---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSnapshotPolicies.html
---

# DescribeSnapshotPolicies

Returns the description of specific Amazon FSx for NetApp ONTAP snapshot policies, if a `SnapshotPolicyIds` value is provided. Otherwise, this operation returns all snapshot policies owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all snapshot policies, you can optionally specify the `MaxResults` parameter to limit the number of snapshot policies in a response. If more snapshot policies remain, Amazon FSx returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

## Request Syntax
<a name="API_DescribeSnapshotPolicies_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SnapshotPolicyIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeSnapshotPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeSnapshotPolicies_RequestSyntax) **   <a name="FSx-DescribeSnapshotPolicies-request-Filters"></a>
The filters structure. The supported names are `file-system-id` or `storage-virtual-machine-id`.
Type: Array of [SnapshotPolicyFilter](API_SnapshotPolicyFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** [MaxResults](#API_DescribeSnapshotPolicies_RequestSyntax) **   <a name="FSx-DescribeSnapshotPolicies-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** [NextToken](#API_DescribeSnapshotPolicies_RequestSyntax) **   <a name="FSx-DescribeSnapshotPolicies-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
Required: No

 ** [SnapshotPolicyIds](#API_DescribeSnapshotPolicies_RequestSyntax) **   <a name="FSx-DescribeSnapshotPolicies-request-SnapshotPolicyIds"></a>
The IDs of the snapshot policies that you want to retrieve. If you also specify `Filters`, only snapshot policies that match both the IDs and the filters are returned. If any IDs aren't found, or if a filter excludes any of them, a `SnapshotPolicyNotFound` error occurs.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Fixed length of 29.
Pattern: `^snapshotpol-[0-9a-f]{17}$`
Required: No

## Response Syntax
<a name="API_DescribeSnapshotPolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SnapshotPolicies": [
      {
         "Enabled": boolean,
         "FileSystemId": "string",
         "Lifecycle": "string",
         "LifecycleTransitionReason": {
            "Message": "string",
            "OntapError": {
               "Code": "string",
               "Message": "string"
            }
         },
         "Name": "string",
         "ResourceARN": "string",
         "Schedules": [
            {
               "Count": number,
               "Name": "string",
               "Prefix": "string",
               "RetentionPeriod": {
                  "Type": "string",
                  "Value": number
               },
               "SnapmirrorLabel": "string"
            }
         ],
         "Scope": "string",
         "SnapshotPolicyId": "string",
         "StorageVirtualMachineId": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "UUID": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSnapshotPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSnapshotPolicies_ResponseSyntax) **   <a name="FSx-DescribeSnapshotPolicies-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`

 ** [SnapshotPolicies](#API_DescribeSnapshotPolicies_ResponseSyntax) **   <a name="FSx-DescribeSnapshotPolicies-response-SnapshotPolicies"></a>
Describes each snapshot policy returned by the `DescribeSnapshotPolicies` operation.
Type: Array of [SnapshotPolicy](API_SnapshotPolicy.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribeSnapshotPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **
A generic error indicating a server-side failure.
 ** Message **
A detailed error message.
HTTP Status Code: 500

 ** SnapshotPolicyNotFound **
No Amazon FSx snapshot policies were found based on the supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSnapshotPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeSnapshotPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeSnapshotPolicies)
