---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_Environment.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# Environment
<a name="API_Environment"></a>

Represents an FinSpace environment.

## Contents
<a name="API_Environment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** awsAccountId **   <a name="finspace-Type-Environment-awsAccountId"></a>
The ID of the AWS account in which the FinSpace environment is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** dedicatedServiceAccountId **   <a name="finspace-Type-Environment-dedicatedServiceAccountId"></a>
The AWS account ID of the dedicated service account associated with your FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** description **   <a name="finspace-Type-Environment-description"></a>
The description of the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** environmentArn **   <a name="finspace-Type-Environment-environmentArn"></a>
The Amazon Resource Name (ARN) of your FinSpace environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`
Required: No

 ** environmentId **   <a name="finspace-Type-Environment-environmentId"></a>
The identifier of the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** environmentUrl **   <a name="finspace-Type-Environment-environmentUrl"></a>
The sign-in URL for the web application of your FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^https?://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** federationMode **   <a name="finspace-Type-Environment-federationMode"></a>
The authentication mode for the environment.
Type: String
Valid Values: `FEDERATED | LOCAL`
Required: No

 ** federationParameters **   <a name="finspace-Type-Environment-federationParameters"></a>
Configuration information when authentication mode is FEDERATED.
Type: [FederationParameters](API_FederationParameters.md) object
Required: No

 ** kmsKeyId **   <a name="finspace-Type-Environment-kmsKeyId"></a>
The KMS key id used to encrypt in the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/]*$`
Required: No

 ** name **   <a name="finspace-Type-Environment-name"></a>
The name of the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$`
Required: No

 ** sageMakerStudioDomainUrl **   <a name="finspace-Type-Environment-sageMakerStudioDomainUrl"></a>
The URL of the integrated FinSpace notebook environment in your web application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/.]*$`
Required: No

 ** status **   <a name="finspace-Type-Environment-status"></a>
The current status of creation of the FinSpace environment.
Type: String
Valid Values: `CREATE_REQUESTED | CREATING | CREATED | DELETE_REQUESTED | DELETING | DELETED | FAILED_CREATION | RETRY_DELETION | FAILED_DELETION | UPDATE_NETWORK_REQUESTED | UPDATING_NETWORK | FAILED_UPDATING_NETWORK | SUSPENDED`
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/Environment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
