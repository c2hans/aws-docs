---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore IdentityProviderConfiguration
<a name="aws-properties-healthlake-fhirdatastore-identityproviderconfiguration"></a>

The identity provider configuration selected when the data store was created.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-identityproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-identityproviderconfiguration-syntax.json"></a>

```
{
  "[AuthorizationStrategy](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy)" : {{String}},
  "[FineGrainedAuthorizationEnabled](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled)" : {{Boolean}},
  "[IdpLambdaArn](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn)" : {{String}},
  "[Metadata](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-identityproviderconfiguration-syntax.yaml"></a>

```
  [AuthorizationStrategy](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy): {{String}}
  [FineGrainedAuthorizationEnabled](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled): {{Boolean}}
  [IdpLambdaArn](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn): {{String}}
  [Metadata](#cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-identityproviderconfiguration-properties"></a>

`AuthorizationStrategy`  <a name="cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy"></a>
The authorization strategy selected when the AWS HealthLake data store is created.
AWS HealthLake provides support for both SMART on FHIR V1 and V2 as described below.
+ `SMART_ON_FHIR_V1` – Support for only SMART on FHIR V1, which includes `read` (read/search) and `write` (create/update/delete) permissions.
+ `SMART_ON_FHIR` – Support for both SMART on FHIR V1 and V2, which includes `create`, `read`, `update`, `delete`, and `search` permissions.
+ `AWS_AUTH` – The default AWS HealthLake authorization strategy; not affiliated with SMART on FHIR.
*Required*: Yes
*Type*: String
*Allowed values*: `SMART_ON_FHIR_V1 | AWS_AUTH | SMART_ON_FHIR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FineGrainedAuthorizationEnabled`  <a name="cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled"></a>
The parameter to enable SMART on FHIR fine-grained authorization for the data store.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdpLambdaArn`  <a name="cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn"></a>
The Amazon Resource Name (ARN) of the Lambda function to use to decode the access token created by the authorization server.
*Required*: No
*Type*: String
*Pattern*: `arn:aws[-a-z]*:lambda:[a-z]{2}-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9\-_\.]+(:(\$LATEST|[a-zA-Z0-9\-_]+))?`
*Minimum*: `49`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Metadata`  <a name="cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata"></a>
The JSON metadata elements to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see [Metadata](https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata) in SMART's App Launch specification.
`authorization_endpoint`: The URL to the OAuth2 authorization endpoint.
`grant_types_supported`: An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are `authorization_code` and `client_credentials`.
`token_endpoint`: The URL to the OAuth2 token endpoint.
`capabilities`: An array of strings of the SMART capabilities that the authorization server supports.
`code_challenge_methods_supported`: An array of strings of supported PKCE code challenge methods. You must include the `S256` method in the array of PKCE code challenge methods.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
