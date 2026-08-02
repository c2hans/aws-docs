---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_VpcIngressConnection.html
---

# VpcIngressConnection
<a name="API_VpcIngressConnection"></a>

The AWS App Runner resource that specifies an App Runner endpoint for incoming traffic. It establishes a connection between a VPC interface endpoint and a App Runner service, to make your App Runner service accessible from only within an Amazon VPC.

## Contents
<a name="API_VpcIngressConnection_Contents"></a>

 ** AccountId **   <a name="apprunner-Type-VpcIngressConnection-AccountId"></a>
The Account Id you use to create the VPC Ingress Connection resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** CreatedAt **   <a name="apprunner-Type-VpcIngressConnection-CreatedAt"></a>
The time when the VPC Ingress Connection was created. It's in the Unix time stamp format.
+  Type: Timestamp
+  Required: Yes
Type: Timestamp
Required: No

 ** DeletedAt **   <a name="apprunner-Type-VpcIngressConnection-DeletedAt"></a>
The time when the App Runner service was deleted. It's in the Unix time stamp format.
+  Type: Timestamp
+  Required: No
Type: Timestamp
Required: No

 ** DomainName **   <a name="apprunner-Type-VpcIngressConnection-DomainName"></a>
The domain name associated with the VPC Ingress Connection resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9*.-]{1,255}`
Required: No

 ** IngressVpcConfiguration **   <a name="apprunner-Type-VpcIngressConnection-IngressVpcConfiguration"></a>
Specifications for the customer’s VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.
Type: [IngressVpcConfiguration](API_IngressVpcConfiguration.md) object
Required: No

 ** ServiceArn **   <a name="apprunner-Type-VpcIngressConnection-ServiceArn"></a>
The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** Status **   <a name="apprunner-Type-VpcIngressConnection-Status"></a>
The current status of the VPC Ingress Connection. The VPC Ingress Connection displays one of the following statuses: `AVAILABLE`, `PENDING_CREATION`, `PENDING_UPDATE`, `PENDING_DELETION`,`FAILED_CREATION`, `FAILED_UPDATE`, `FAILED_DELETION`, and `DELETED`..
Type: String
Valid Values: `AVAILABLE | PENDING_CREATION | PENDING_UPDATE | PENDING_DELETION | FAILED_CREATION | FAILED_UPDATE | FAILED_DELETION | DELETED`
Required: No

 ** VpcIngressConnectionArn **   <a name="apprunner-Type-VpcIngressConnection-VpcIngressConnectionArn"></a>
The Amazon Resource Name (ARN) of the VPC Ingress Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** VpcIngressConnectionName **   <a name="apprunner-Type-VpcIngressConnection-VpcIngressConnectionName"></a>
The customer-provided VPC Ingress Connection name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,39}`
Required: No

## See Also
<a name="API_VpcIngressConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/VpcIngressConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/VpcIngressConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/VpcIngressConnection)
