---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ListenerSummary.html
---

# ListenerSummary
<a name="API_ListenerSummary"></a>

Summary information about a listener.

## Contents
<a name="API_ListenerSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ListenerSummary-arn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ListenerSummary-createdAt"></a>
The date and time that the listener was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** id **   <a name="vpclattice-Type-ListenerSummary-id"></a>
The ID of the listener.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `listener-[0-9a-z]{17}`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ListenerSummary-lastUpdatedAt"></a>
The date and time that the listener was last updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-ListenerSummary-name"></a>
The name of the listener.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!listener-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** port **   <a name="vpclattice-Type-ListenerSummary-port"></a>
The listener port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** protocol **   <a name="vpclattice-Type-ListenerSummary-protocol"></a>
The listener protocol.
Type: String
Valid Values: `HTTP | HTTPS | TLS_PASSTHROUGH`
Required: No

## See Also
<a name="API_ListenerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ListenerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ListenerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ListenerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
