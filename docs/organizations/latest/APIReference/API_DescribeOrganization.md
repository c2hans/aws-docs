---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeOrganization.html
---

# DescribeOrganization
<a name="API_DescribeOrganization"></a>

Retrieves information about the organization that the user's account belongs to.

You can call this operation from any account in a organization.

**Note**
Even if a policy type is shown as available in the organization, you can disable it separately at the root level with [DisablePolicyType](API_DisablePolicyType.md). Use [ListRoots](API_ListRoots.md) to see the status of policy types for a specified root.

## Response Syntax
<a name="API_DescribeOrganization_ResponseSyntax"></a>

```
{
   "Organization": {
      "Arn": "string",
      "AvailablePolicyTypes": [
         {
            "Status": "string",
            "Type": "string"
         }
      ],
      "FeatureSet": "string",
      "Id": "string",
      "MasterAccountArn": "string",
      "MasterAccountEmail": "string",
      "MasterAccountId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Organization](#API_DescribeOrganization_ResponseSyntax) **   <a name="organizations-DescribeOrganization-response-Organization"></a>
A structure that contains information about the organization.
The `AvailablePolicyTypes` part of the response is deprecated, and you shouldn't use it in your apps. It doesn't include any policy type supported by Organizations other than SCPs. In the China (Ningxia) Region, no policy type is included. To determine which policy types are enabled in your organization, use the ` ListRoots ` operation.
Type: [Organization](API_Organization.md) object

## Errors
<a name="API_DescribeOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 400

 ** AWSOrganizationsNotInUseException **
Your account isn't a member of an organization. To make this request, you must use the credentials of an account that belongs to an organization.
HTTP Status Code: 400

 ** ConcurrentModificationException **
The target of the operation is currently being modified by a different request. Try again later.
HTTP Status Code: 400

 ** ServiceException **
 AWS Organizations can't complete your request because of an internal service error. Try again later.
HTTP Status Code: 500

 ** TooManyRequestsException **
You have sent too many requests in too short a period of time. The quota helps protect against denial-of-service attacks. Try again later.
For information about quotas that affect AWS Organizations, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the * AWS Organizations User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_DescribeOrganization_Examples"></a>

### Example
<a name="API_DescribeOrganization_Example_1"></a>

The following example shows how to request information about the current user's organization.

#### Sample Request
<a name="API_DescribeOrganization_Example_1_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSOrganizationsV20161128.DescribeOrganization

{}
```

#### Sample Response
<a name="API_DescribeOrganization_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
{
  "Organization": {
    "MasterAccountArn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
    "MasterAccountEmail": "diego@example.com",
    "MasterAccountId": "111111111111",
    "Id": "o-exampleorgid",
    "FeatureSet": "ALL",
    "Arn": "arn:aws:organizations::111111111111:organization/o-exampleorgid",
    "AvailablePolicyTypes": [ ...DEPRECATED – DO NOT USE... ]
    ]
  }
}
```

## See Also
<a name="API_DescribeOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/organizations-2016-11-28/DescribeOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/DescribeOrganization)
