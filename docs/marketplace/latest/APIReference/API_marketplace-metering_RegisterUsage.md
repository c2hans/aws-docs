---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_RegisterUsage.html
---

# RegisterUsage
<a name="API_marketplace-metering_RegisterUsage"></a>

Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the `RegisterUsage` operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren't required to call `RegisterUsage`, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of `RegisterUsage`. `RegisterUsage` performs two primary functions: metering and entitlement.
+  *Entitlement*: `RegisterUsage` allows you to verify that the customer running your paid software is subscribed to your product on AWS Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with `RegisterUsage` is only required to guard against unauthorized use at container startup, as such a `CustomerNotSubscribedException` or `PlatformNotSupportedException` will only be thrown on the initial call to `RegisterUsage`. Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a `CustomerNotSubscribedException`, even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.
+  *Metering*: `RegisterUsage` meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged for 10 tasks. Software metering is handled by the AWS Marketplace metering control plane—your software is not required to perform metering-specific actions other than to call `RegisterUsage` to commence metering. The AWS Marketplace metering control plane will also bill customers for running ECS tasks and Amazon EKS pods, regardless of the customer's subscription state, which removes the need for your software to run entitlement checks at runtime. For containers, `RegisterUsage` should be called immediately at launch. If you don’t register the container within the first 6 hours of the launch, AWS Marketplace Metering Service doesn’t provide any metering guarantees for previous months. Metering will continue, however, for the current month forward until the container ends. `RegisterUsage` is for metering paid hourly container products.

  For AWS Regions that support `RegisterUsage`, see [RegisterUsage Region support](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#registerusage-region-support).

## Request Syntax
<a name="API_marketplace-metering_RegisterUsage_RequestSyntax"></a>

```
{
   "Nonce": "{{string}}",
   "ProductCode": "{{string}}",
   "PublicKeyVersion": {{number}}
}
```

## Request Parameters
<a name="API_marketplace-metering_RegisterUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ProductCode](#API_marketplace-metering_RegisterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_RegisterUsage-request-ProductCode"></a>
Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[-a-zA-Z0-9/=:_.@]*$`
Required: Yes

 ** [PublicKeyVersion](#API_marketplace-metering_RegisterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_RegisterUsage-request-PublicKeyVersion"></a>
Public Key Version provided by AWS Marketplace
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [Nonce](#API_marketplace-metering_RegisterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_RegisterUsage-request-Nonce"></a>
(Optional) To scope down the registration to a specific running software instance and guard against replay attacks.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_marketplace-metering_RegisterUsage_ResponseSyntax"></a>

```
{
   "PublicKeyRotationTimestamp": number,
   "Signature": "string"
}
```

## Response Elements
<a name="API_marketplace-metering_RegisterUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PublicKeyRotationTimestamp](#API_marketplace-metering_RegisterUsage_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_RegisterUsage-response-PublicKeyRotationTimestamp"></a>
(Optional) Only included when public key version has expired
Type: Timestamp

 ** [Signature](#API_marketplace-metering_RegisterUsage_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_RegisterUsage-response-Signature"></a>
JWT Token
Type: String
Pattern: `[\s\S]+`

## Errors
<a name="API_marketplace-metering_RegisterUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomerNotEntitledException **
Exception thrown when the customer does not have a valid subscription for the product.
HTTP Status Code: 400

 ** DisabledApiException **
The API is disabled in the Region.
HTTP Status Code: 400

 ** InternalServiceErrorException **
An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.
HTTP Status Code: 500

 ** InvalidProductCodeException **
The product code passed does not match the product code used for publishing the product.
HTTP Status Code: 400

 ** InvalidPublicKeyVersionException **
Public Key version is invalid.
HTTP Status Code: 400

 ** InvalidRegionException **
 `RegisterUsage` must be called in the same AWS Region the ECS task was launched in. This prevents a container from hardcoding a Region (e.g. withRegion(“us-east-1”) when calling `RegisterUsage`.
HTTP Status Code: 400

 ** PlatformNotSupportedException **
 AWS Marketplace does not support metering usage from the underlying platform. Currently, Amazon ECS, Amazon EKS, and AWS Fargate are supported.
HTTP Status Code: 400

 ** ThrottlingException **
The calls to the API are throttled.
HTTP Status Code: 400

## Examples
<a name="API_marketplace-metering_RegisterUsage_Examples"></a>

### Example
<a name="API_marketplace-metering_RegisterUsage_Example_1"></a>

Below are the sample request and response for `RegisterUsage`

#### Sample Request
<a name="API_marketplace-metering_RegisterUsage_Example_1_Request"></a>

```
{
    "ProductCode" : "cqcvf9f0ugw8rkbgmf1c9dxyz",
    "PublicKeyVersion": 1,
    "Nonce": "2ead20e4-3e6d-42cd-8f56-24f02d1cc4e1"
}
```

#### Sample Response
<a name="API_marketplace-metering_RegisterUsage_Example_1_Response"></a>

```
{
   "PublicKeyRotationTimestamp": null,
   "Signature": "eyJhbGciOiJQUzI1Ni..."
}

// Where the signature is composed of 3 dot-separated,
// base-64 URL Encoded sections.
// e.g. eyJhbGcVCJ9.eyJzdWIMzkwMjJ9.rrO9Qw0SXRWTe

// Section 1: Header/Algorithm

{
  "alg": "PS256",
  "typ": "JWT"
}

// Section 2: Payload

{
   "ProductCode" : "cqcvf9f0ugw8rkbgmf1c9dxyz",
   "PublicKeyVersion": 1,
   "Nonce": "2ead20e4-3e6d-42cd-8f56-24f02d1cc4e1",
   "PublicKeyRotationTimestamp": null
}

// Section 3: RSA-PSS SHA256 signature

"rrO9Q4FEi3gweH3X4lrt2okf5zwIatUUwERlw016wTy_21Nv8S..."
```

## See Also
<a name="API_marketplace-metering_RegisterUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/meteringmarketplace-2016-01-14/RegisterUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/RegisterUsage)
