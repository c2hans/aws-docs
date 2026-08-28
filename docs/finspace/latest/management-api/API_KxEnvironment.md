---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxEnvironment.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxEnvironment
<a name="API_KxEnvironment"></a>

The details of a kdb environment.

## Contents
<a name="API_KxEnvironment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZoneIds **   <a name="finspace-Type-KxEnvironment-availabilityZoneIds"></a>
The identifier of the availability zones where subnets for the environment are created.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** awsAccountId **   <a name="finspace-Type-KxEnvironment-awsAccountId"></a>
The unique identifier of the AWS account in which you create the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** certificateAuthorityArn **   <a name="finspace-Type-KxEnvironment-certificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the certificate authority:
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** creationTimestamp **   <a name="finspace-Type-KxEnvironment-creationTimestamp"></a>
The timestamp at which the kdb environment was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** customDNSConfiguration **   <a name="finspace-Type-KxEnvironment-customDNSConfiguration"></a>
A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.
Type: Array of [CustomDNSServer](API_CustomDNSServer.md) objects
Required: No

 ** dedicatedServiceAccountId **   <a name="finspace-Type-KxEnvironment-dedicatedServiceAccountId"></a>
A unique identifier for the AWS environment infrastructure account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** description **   <a name="finspace-Type-KxEnvironment-description"></a>
A description of the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** dnsStatus **   <a name="finspace-Type-KxEnvironment-dnsStatus"></a>
The status of DNS configuration.
Type: String
Valid Values: `NONE | UPDATE_REQUESTED | UPDATING | FAILED_UPDATE | SUCCESSFULLY_UPDATED`
Required: No

 ** environmentArn **   <a name="finspace-Type-KxEnvironment-environmentArn"></a>
The Amazon Resource Name (ARN) of your kdb environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`
Required: No

 ** environmentId **   <a name="finspace-Type-KxEnvironment-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: No

 ** errorMessage **   <a name="finspace-Type-KxEnvironment-errorMessage"></a>
Specifies the error message that appears if a flow fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** kmsKeyId **   <a name="finspace-Type-KxEnvironment-kmsKeyId"></a>
The unique identifier of the KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/]*$`
Required: No

 ** name **   <a name="finspace-Type-KxEnvironment-name"></a>
The name of the kdb environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** status **   <a name="finspace-Type-KxEnvironment-status"></a>
The status of the environment creation.
+ CREATE\_REQUESTED – Environment creation has been requested.
+ CREATING – Environment is in the process of being created.
+ FAILED\_CREATION – Environment creation has failed.
+ CREATED – Environment is successfully created and is currently active.
+ DELETE REQUESTED – Environment deletion has been requested.
+ DELETING – Environment is in the process of being deleted.
+ RETRY\_DELETION – Initial environment deletion failed, system is reattempting delete.
+ DELETED – Environment has been deleted.
+ FAILED\_DELETION – Environment deletion has failed.
Type: String
Valid Values: `CREATE_REQUESTED | CREATING | CREATED | DELETE_REQUESTED | DELETING | DELETED | FAILED_CREATION | RETRY_DELETION | FAILED_DELETION | UPDATE_NETWORK_REQUESTED | UPDATING_NETWORK | FAILED_UPDATING_NETWORK | SUSPENDED`
Required: No

 ** tgwStatus **   <a name="finspace-Type-KxEnvironment-tgwStatus"></a>
The status of the network configuration.
Type: String
Valid Values: `NONE | UPDATE_REQUESTED | UPDATING | FAILED_UPDATE | SUCCESSFULLY_UPDATED`
Required: No

 ** transitGatewayConfiguration **   <a name="finspace-Type-KxEnvironment-transitGatewayConfiguration"></a>
Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.
Type: [TransitGatewayConfiguration](API_TransitGatewayConfiguration.md) object
Required: No

 ** updateTimestamp **   <a name="finspace-Type-KxEnvironment-updateTimestamp"></a>
The timestamp at which the kdb environment was modified in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

## See Also
<a name="API_KxEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
