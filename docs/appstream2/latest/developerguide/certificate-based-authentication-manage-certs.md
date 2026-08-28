---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-certs.html
---

# End User Certificates
<a name="certificate-based-authentication-manage-certs"></a>

End user certificates issued by AWS Private CA for WorkSpaces Applications certificate-based authentication don't require renewal or revocation. These certificates are short-lived. WorkSpaces Applications automatically issues a new certificate for each new session, or every 24 hours for sessions with a long duration. The WorkSpaces Applications session governs the use of these end user certificates. If you end a session, WorkSpaces Applications stops using that certificate. These end user certificates have a shorter validity period than a typical AWS Private CA CRL distribution. As a result, end user certificates don't need to be revoked and won't appear in a CRL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
