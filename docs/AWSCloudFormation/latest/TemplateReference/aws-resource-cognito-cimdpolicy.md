---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-cimdpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::CIMDPolicy

Creates a Client ID Metadata Document (CIMD) policy for an app client. With a CIMD policy, OAuth clients can identify themselves to your user pool with an HTTPS URL as their client ID. Amazon Cognito retrieves the client metadata document from that URL and accepts the client only when the URL matches one of the URL patterns in the policy.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Syntax
<a name="aws-resource-cognito-cimdpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-cimdpolicy-syntax.json"></a>

```json
{
  "Type" : "AWS::Cognito::CIMDPolicy",
  "Properties" : {
      "[CacheDuration](#cfn-cognito-cimdpolicy-cacheduration)" : {{Integer}},
      "[ClientId](#cfn-cognito-cimdpolicy-clientid)" : {{String}},
      "[PolicyName](#cfn-cognito-cimdpolicy-policyname)" : {{String}},
      "[URLPatterns](#cfn-cognito-cimdpolicy-urlpatterns)" : {{[ String, ... ]}},
      "[UserPoolId](#cfn-cognito-cimdpolicy-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-cimdpolicy-syntax.yaml"></a>

```yaml
Type: AWS::Cognito::CIMDPolicy
Properties:
  [CacheDuration](#cfn-cognito-cimdpolicy-cacheduration): {{Integer}}
  [ClientId](#cfn-cognito-cimdpolicy-clientid): {{String}}
  [PolicyName](#cfn-cognito-cimdpolicy-policyname): {{String}}
  [URLPatterns](#cfn-cognito-cimdpolicy-urlpatterns): {{
    - String}}
  [UserPoolId](#cfn-cognito-cimdpolicy-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-cimdpolicy-properties"></a>

`CacheDuration`  <a name="cfn-cognito-cimdpolicy-cacheduration"></a>
The length of time, in seconds, that Amazon Cognito caches a client metadata document when the document's `Cache-Control` header doesn't set a `max-age` between one day and one year. When the header sets a `max-age` in that range, Amazon Cognito uses the header value instead.
*Required*: No
*Type*: Integer
*Minimum*: `86400`
*Maximum*: `31556952`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-cognito-cimdpolicy-clientid"></a>
The ID of the app client that the CIMD policy is associated with. Amazon Cognito omits this value when the app client no longer exists.
*Required*: Yes
*Type*: String
*Pattern*: `[\w+]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-cognito-cimdpolicy-policyname"></a>
The friendly name of the CIMD policy.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{M}\p{S}\p{N}\p{P}\p{Z}]+`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLPatterns`  <a name="cfn-cognito-cimdpolicy-urlpatterns"></a>
The HTTPS URL patterns that a client ID metadata document URL must match. Each pattern contains at most one `*` wildcard.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-cimdpolicy-userpoolid"></a>
The ID of the user pool that contains the CIMD policy.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-cimdpolicy-return-values"></a>

### Ref
<a name="aws-resource-cognito-cimdpolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cognito-cimdpolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-cognito-cimdpolicy-return-values-fn--getatt-fn--getatt"></a>

`CIMDPolicyId`  <a name="CIMDPolicyId-fn::getatt"></a>
The ID of the CIMD policy.
