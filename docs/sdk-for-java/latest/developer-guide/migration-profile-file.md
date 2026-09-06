---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-profile-file.html
---

# Profile file changes
<a name="migration-profile-file"></a>

The AWS SDK for Java 2.x parses the profile definitions in `~/.aws/config` and `~/.aws/credentials` to more closely emulate the way the AWS CLI parses the files.

The SDK for Java 2.x:
+ Resolves a `~/` or `~` followed by the file system's default path separator at the start of the path by checking, in order, `$HOME`, `$USERPROFILE` (Windows only), `$HOMEDRIVE`, `$HOMEPATH` (Windows only), and then the `user.home` system property.
+ Looks for the `AWS_SHARED_CREDENTIALS_FILE` environment variable instead of `AWS_CREDENTIAL_PROFILES_FILE`.
+ Silently drops profile definitions in configuration files without the word `profile` at the beginning of the profile name.
+ Silently drops profile definitions that do not consist of alphanumeric, underscore or dash characters (after the leading `profile` word has been removed for configuration files).
+ Merges settings of profile definitions duplicated within the same file.
+ Merges settings of profile definitions duplicated in both the configuration and credentials files.
+ Does NOT merge settings if both `[profile foo]` and `[foo]` are found in the same file.
+ Uses settings in `[profile foo]` if both `[profile foo]` and `[foo]` are found in the configuration file.
+ Uses the value of the last duplicated setting in the same file and profile.
+ Recognizes both `;` and `#` for defining a comment.
+ Recognizes `;` and `#` in profile definitions to define a comment, even if the characters are adjacent to the closing bracket.
+ Recognizes `;` and `#` to define a comment only in setting values only if they are preceded by whitespace.
+ Recognizes `;` and `#` and all following content in setting values if they are not preceded by whitespace.
+ Considers role-based credentials the highest-priority credentials. The 2.x SDK always uses role-based credentials if the user specifies the `role_arn` property.
+ Considers session-based credentials the second-highest-priority credentials. The 2.x SDK always uses session-based credentials if role-based credentials were not used and the user specifies the `aws_access_key_id` and `aws_session_token` properties.
+ Uses basic credentials if role-based and session-based credentials are not used and the user specified the `aws_access_key_id` property.
