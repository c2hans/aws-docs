---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/data-encryption.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Data encryption
<a name="data-encryption"></a>

WorkSpaces Thin Client collects environment and device customization data, such as user settings, device identifiers, identity provider information, and streaming desktop identifiers. WorkSpaces Thin Client also collects session timestamps. Collected data is stored in Amazon DynamoDB and Amazon S3. WorkSpaces Thin Client uses AWS Key Management Service (KMS) for encryption.

To secure your content, follow these guidelines:
+ Implement least privilege access and create specific roles to be used for WorkSpaces Thin Client actions.
+ Protect data end-to-end by providing a customer-managed key, so WorkSpaces Thin Client can encrypt your data at rest with the keys you supply.
+ Be careful with sharing environment activation codes and user credentials:
  + Admins are required to log into the WorkSpaces Thin Client console, and users are required to provide activation codes for WorkSpaces Thin Client setup use credentials to log into the streaming desktop.
  + Anyone with physical access can set up a WorkSpaces Thin Client, but they can't start a session unless they have a valid activation code and user credentials to log in.
+ Users can explicitly end their sessions by choosing to lock their screen, reboot, or shut down the device by using the device toolbar. This discards the device session and clears session credentials.

WorkSpaces Thin Client secures content and metadata by default by encrypting all sensitive data with AWS KMS. If there is an error applying existing settings, a user can't access new sessions and devices cannot apply software updates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
