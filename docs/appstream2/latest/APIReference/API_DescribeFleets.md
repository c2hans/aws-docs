---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeFleets.html
---

# DescribeFleets
<a name="API_DescribeFleets"></a>

Retrieves a list that describes one or more specified fleets, if the fleet names are provided. Otherwise, all fleets in the account are described.

## Request Syntax
<a name="API_DescribeFleets_RequestSyntax"></a>

```
{
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Names](#API_DescribeFleets_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeFleets-request-Names"></a>
The names of the fleets to describe.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [NextToken](#API_DescribeFleets_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeFleets-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeFleets_ResponseSyntax"></a>

```
{
   "Fleets": [
      {
         "Arn": "string",
         "ComputeCapacityStatus": {
            "ActiveUserSessions": number,
            "ActualUserSessions": number,
            "Available": number,
            "AvailableUserSessions": number,
            "Desired": number,
            "DesiredUserSessions": number,
            "Draining": number,
            "DrainModeActiveUserSessions": number,
            "DrainModeUnusedUserSessions": number,
            "InUse": number,
            "Running": number
         },
         "CreatedTime": number,
         "Description": "string",
         "DisableIMDSV1": boolean,
         "DisconnectTimeoutInSeconds": number,
         "DisplayName": "string",
         "DomainJoinInfo": {
            "DirectoryName": "string",
            "OrganizationalUnitDistinguishedName": "string"
         },
         "EnableDefaultInternetAccess": boolean,
         "FleetErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "FleetType": "string",
         "IamRoleArn": "string",
         "IdleDisconnectTimeoutInSeconds": number,
         "ImageArn": "string",
         "ImageName": "string",
         "InstanceType": "string",
         "MaxConcurrentSessions": number,
         "MaxSessionsPerInstance": number,
         "MaxUserDurationInSeconds": number,
         "Name": "string",
         "Platform": "string",
         "RootVolumeConfig": {
            "VolumeSizeInGb": number
         },
         "SessionScriptS3Location": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "State": "string",
         "StreamView": "string",
         "UsbDeviceFilterStrings": [ "string" ],
         "VpcConfig": {
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ]
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Fleets](#API_DescribeFleets_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeFleets-response-Fleets"></a>
Information about the fleets.
Type: Array of [Fleet](API_Fleet.md) objects

 ** [NextToken](#API_DescribeFleets_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeFleets-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeFleets)
