---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_Network.html
---

# Network
<a name="API_Network"></a>

Represents a Wickr network with all its configuration and status information.

## Contents
<a name="API_Network_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accessLevel **   <a name="wickr-Type-Network-accessLevel"></a>
The access level of the network (STANDARD or PREMIUM), which determines available features and capabilities.
Type: String
Valid Values: `STANDARD | PREMIUM`
Required: Yes

 ** awsAccountId **   <a name="wickr-Type-Network-awsAccountId"></a>
The AWS account ID that owns the network.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** networkArn **   <a name="wickr-Type-Network-networkArn"></a>
The Amazon Resource Name (ARN) of the network.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** networkId **   <a name="wickr-Type-Network-networkId"></a>
The unique identifier of the network.
Type: String
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: Yes

 ** networkName **   <a name="wickr-Type-Network-networkName"></a>
The name of the network.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** encryptionKeyArn **   <a name="wickr-Type-Network-encryptionKeyArn"></a>
The ARN of the AWS KMS customer managed key used for encrypting sensitive data in the network.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** freeTrialExpiration **   <a name="wickr-Type-Network-freeTrialExpiration"></a>
The expiration date and time for the network's free trial period, if applicable.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** migrationState **   <a name="wickr-Type-Network-migrationState"></a>
The SSO redirect URI migration state, managed by the SSO redirect migration wizard. Values: 0 (not started), 1 (in progress), or 2 (completed).
Type: Integer
Required: No

 ** standing **   <a name="wickr-Type-Network-standing"></a>
The current standing or status of the network.
Type: Integer
Required: No

## See Also
<a name="API_Network_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/Network)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/Network)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/Network)
