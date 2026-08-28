---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-terms.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::Terms
<a name="aws-resource-cognito-terms"></a>

Creates terms documents for the requested app client. When Terms and conditions and Privacy policy documents are configured, the app client displays links to them in the sign-up page of managed login for the app client.

You can provide URLs for terms documents in the languages that are supported by [managed login localization](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization). Amazon Cognito directs users to the terms documents for their current language, with fallback to `default` if no document exists for the language.

Each request accepts one type of terms document and a map of language-to-link for that document type. You must provide both types of terms documents in at least one language before Amazon Cognito displays your terms documents. Supply each type in separate requests.

For more information, see [Terms documents](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-terms-documents).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Syntax
<a name="aws-resource-cognito-terms-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-terms-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::Terms",
  "Properties" : {
      "[ClientId](#cfn-cognito-terms-clientid)" : {{String}},
      "[Enforcement](#cfn-cognito-terms-enforcement)" : {{String}},
      "[Links](#cfn-cognito-terms-links)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TermsName](#cfn-cognito-terms-termsname)" : {{String}},
      "[TermsSource](#cfn-cognito-terms-termssource)" : {{String}},
      "[UserPoolId](#cfn-cognito-terms-userpoolid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-terms-syntax.yaml"></a>

```
Type: AWS::Cognito::Terms
Properties:
  [ClientId](#cfn-cognito-terms-clientid): {{String}}
  [Enforcement](#cfn-cognito-terms-enforcement): {{String}}
  [Links](#cfn-cognito-terms-links): {{
    {{Key}}: {{Value}}}}
  [TermsName](#cfn-cognito-terms-termsname): {{String}}
  [TermsSource](#cfn-cognito-terms-termssource): {{String}}
  [UserPoolId](#cfn-cognito-terms-userpoolid): {{String}}
```

## Properties
<a name="aws-resource-cognito-terms-properties"></a>

`ClientId`  <a name="cfn-cognito-terms-clientid"></a>
The ID of the app client that the terms documents are assigned to.
*Required*: No
*Type*: String
*Pattern*: `[\w+]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Enforcement`  <a name="cfn-cognito-terms-enforcement"></a>
This parameter is reserved for future use and currently accepts one value.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Links`  <a name="cfn-cognito-terms-links"></a>
A map of URLs to languages. For each localized language that will view the requested `TermsName`, assign a URL. A selection of `cognito:default` displays for all languages that don't have a language-specific URL.
For example, `"cognito:default": "https://terms.example.com", "cognito:spanish": "https://terms.example.com/es"`.
*Required*: Yes
*Type*: Object of String
*Pattern*: `^cognito:(default|english|french|spanish|german|bahasa-indonesia|italian|japanese|korean|portuguese-brazil|chinese-(simplified|traditional))$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TermsName`  <a name="cfn-cognito-terms-termsname"></a>
The type and friendly name of the terms documents.
*Required*: Yes
*Type*: String
*Pattern*: `^(terms-of-use|privacy-policy)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TermsSource`  <a name="cfn-cognito-terms-termssource"></a>
This parameter is reserved for future use and currently accepts one value.
*Required*: Yes
*Type*: String
*Allowed values*: `LINK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-terms-userpoolid"></a>
The ID of the user pool that contains the terms documents.
*Required*: Yes
*Type*: String
*Pattern*: `[\w-]+_[0-9a-zA-Z]+`
*Minimum*: `1`
*Maximum*: `55`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cognito-terms-return-values"></a>

### Ref
<a name="aws-resource-cognito-terms-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cognito-terms-return-values-fn--getatt"></a>

####
<a name="aws-resource-cognito-terms-return-values-fn--getatt-fn--getatt"></a>

`TermsId`  <a name="TermsId-fn::getatt"></a>
The ID of the terms documents.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
