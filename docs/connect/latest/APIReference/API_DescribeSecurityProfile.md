---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeSecurityProfile.html
---

# DescribeSecurityProfile
<a name="API_DescribeSecurityProfile"></a>

Gets basic information about the security profile.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Request Syntax
<a name="API_DescribeSecurityProfile_RequestSyntax"></a>

```
GET /security-profiles/{{InstanceId}}/{{SecurityProfileId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeSecurityProfile_RequestSyntax) **   <a name="connect-DescribeSecurityProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [SecurityProfileId](#API_DescribeSecurityProfile_RequestSyntax) **   <a name="connect-DescribeSecurityProfile-request-uri-SecurityProfileId"></a>
The identifier for the security profle.
Required: Yes

## Request Body
<a name="API_DescribeSecurityProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SecurityProfile": {
      "AllowedAccessControlHierarchyGroupId": "string",
      "AllowedAccessControlTags": {
         "string" : "string"
      },
      "Arn": "string",
      "Description": "string",
      "GranularAccessControlConfiguration": {
         "DataTableAccessControlConfiguration": {
            "PrimaryAttributeAccessControlConfiguration": {
               "PrimaryAttributeValues": [
                  {
                     "AccessType": "string",
                     "AttributeName": "string",
                     "Values": [ "string" ]
                  }
               ]
            }
         }
      },
      "HierarchyRestrictedResources": [ "string" ],
      "Id": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "OrganizationResourceId": "string",
      "SecurityProfileName": "string",
      "TagRestrictedResources": [ "string" ],
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecurityProfile](#API_DescribeSecurityProfile_ResponseSyntax) **   <a name="connect-DescribeSecurityProfile-response-SecurityProfile"></a>
The security profile.
Type: [SecurityProfile](API_SecurityProfile.md) object

## Errors
<a name="API_DescribeSecurityProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeSecurityProfile)
