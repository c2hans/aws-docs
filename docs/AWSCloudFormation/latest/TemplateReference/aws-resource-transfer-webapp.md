---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-webapp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::WebApp
<a name="aws-resource-transfer-webapp"></a>

Creates a web app based on specified parameters, and returns the ID for the new web app. You can configure the web app to be publicly accessible or hosted within a VPC.

For more information about using VPC endpoints with AWS Transfer Family, see [Create a Transfer Family web app in a VPC](https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html).

## Syntax
<a name="aws-resource-transfer-webapp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-webapp-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::WebApp",
  "Properties" : {
      "[AccessEndpoint](#cfn-transfer-webapp-accessendpoint)" : {{String}},
      "[EndpointDetails](#cfn-transfer-webapp-endpointdetails)" : {{EndpointDetails}},
      "[IdentityProviderDetails](#cfn-transfer-webapp-identityproviderdetails)" : {{IdentityProviderDetails}},
      "[Tags](#cfn-transfer-webapp-tags)" : {{[ Tag, ... ]}},
      "[WebAppCustomization](#cfn-transfer-webapp-webappcustomization)" : {{WebAppCustomization}},
      "[WebAppEndpointPolicy](#cfn-transfer-webapp-webappendpointpolicy)" : {{String}},
      "[WebAppUnits](#cfn-transfer-webapp-webappunits)" : {{WebAppUnits}}
    }
}
```

### YAML
<a name="aws-resource-transfer-webapp-syntax.yaml"></a>

```
Type: AWS::Transfer::WebApp
Properties:
  [AccessEndpoint](#cfn-transfer-webapp-accessendpoint): {{String}}
  [EndpointDetails](#cfn-transfer-webapp-endpointdetails): {{
    EndpointDetails}}
  [IdentityProviderDetails](#cfn-transfer-webapp-identityproviderdetails): {{
    IdentityProviderDetails}}
  [Tags](#cfn-transfer-webapp-tags): {{
    - Tag}}
  [WebAppCustomization](#cfn-transfer-webapp-webappcustomization): {{
    WebAppCustomization}}
  [WebAppEndpointPolicy](#cfn-transfer-webapp-webappendpointpolicy): {{String}}
  [WebAppUnits](#cfn-transfer-webapp-webappunits): {{
    WebAppUnits}}
```

## Properties
<a name="aws-resource-transfer-webapp-properties"></a>

`AccessEndpoint`  <a name="cfn-transfer-webapp-accessendpoint"></a>
The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.
Before you enter a custom URL for this parameter, follow the steps described in [Update your access endpoint with a custom URL](https://docs.aws.amazon.com//transfer/latest/userguide/webapp-customize.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointDetails`  <a name="cfn-transfer-webapp-endpointdetails"></a>
The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the `UpdateServer` API and attach an Elastic IP address to your server's endpoint.
 After May 19, 2021, you won't be able to create a server using `EndpointType=VPC_ENDPOINT` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with `EndpointType=VPC_ENDPOINT` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use `EndpointType`=`VPC`.
For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).
It is recommended that you use `VPC` as the `EndpointType`. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with `EndpointType` set to `VPC_ENDPOINT`.
*Required*: No
*Type*: [EndpointDetails](aws-properties-transfer-webapp-endpointdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderDetails`  <a name="cfn-transfer-webapp-identityproviderdetails"></a>
You can provide a structure that contains the details for the identity provider to use with your web app.
For more details about this parameter, see [Configure your identity provider for Transfer Family web apps](https://docs.aws.amazon.com//transfer/latest/userguide/webapp-identity-center.html).
*Required*: Yes
*Type*: [IdentityProviderDetails](aws-properties-transfer-webapp-identityproviderdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-transfer-webapp-tags"></a>
Key-value pairs that can be used to group and search for web apps. Tags are metadata attached to web apps for any purpose.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-webapp-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAppCustomization`  <a name="cfn-transfer-webapp-webappcustomization"></a>
A structure that contains the customization fields for the web app. You can provide a title, logo, and icon to customize the appearance of your web app.
*Required*: No
*Type*: [WebAppCustomization](aws-properties-transfer-webapp-webappcustomization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAppEndpointPolicy`  <a name="cfn-transfer-webapp-webappendpointpolicy"></a>
 Setting for the type of endpoint policy for the web app. The default value is `STANDARD`.
If your web app was created in an AWS GovCloud (US) Region, the value of this parameter can be `FIPS`, which indicates the web app endpoint is FIPS-compliant.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD | FIPS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WebAppUnits`  <a name="cfn-transfer-webapp-webappunits"></a>
A union that contains the value for number of concurrent connections or the user sessions on your web app.
*Required*: No
*Type*: [WebAppUnits](aws-properties-transfer-webapp-webappunits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-webapp-return-values"></a>

### Ref
<a name="aws-resource-transfer-webapp-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the web app ARN, such as `arn:aws:transfer:us-east-2:123456789012:webapp/webapp-01234567890abcdef` .

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-transfer-webapp-return-values-fn--getatt"></a>

####
<a name="aws-resource-transfer-webapp-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the web app.

`IdentityProviderDetails.ApplicationArn`  <a name="IdentityProviderDetails.ApplicationArn-fn::getatt"></a>
Property description not available.

`VpcEndpointId`  <a name="VpcEndpointId-fn::getatt"></a>
The identifier of the VPC endpoint created for the web app.

`WebAppId`  <a name="WebAppId-fn::getatt"></a>
The unique identifier for the web app.
