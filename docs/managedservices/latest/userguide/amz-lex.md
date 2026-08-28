---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/amz-lex.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Use AMS SSP to provision Amazon Lex in your AMS account
<a name="amz-lex"></a>

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Lex capabilities directly in your AMS managed account. Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text, to enable you to build applications with highly engaging user experiences and lifelike conversational interactions. With Amazon Lex, the same deep learning technologies that power Amazon Alexa are now available to any developer, enabling you to quickly and easily build sophisticated, natural language, conversational bots ﻿or chatbots﻿. To learn more, see [Amazon Lex](https://aws.amazon.com/lex/).

## Amazon Lex in AWS Managed Services FAQ
<a name="set-amz-lex-faqs"></a>

Common questions and answers:

**Q: How do I request access to Amazon Lex in my AMS account?**

Request access by submitting a Management \| AWS service \| Self-provisioned service \| Add change type (ct-1w8z66n899dct). This RFC provisions the following IAM role to your account: `customer_lex_author_role`. Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Lex in my AMS account?**

Amazon Lex integration with Lambda is limited to Lambda functions without an "AMS-" prefix, in order to prevent any modifications to AMS infrastructure.

**Q: What are the prerequisites or dependencies to using Amazon Lex in my AMS account?**

There are no prerequisites or dependencies to use Amazon Lex in your AMS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
