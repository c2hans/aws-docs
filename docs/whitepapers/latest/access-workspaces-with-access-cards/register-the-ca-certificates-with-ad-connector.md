---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/register-the-ca-certificates-with-ad-connector.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Register the CA Certificates with AD Connector
<a name="register-the-ca-certificates-with-ad-connector"></a>

To register your CA certificate in AD Connector, use the following CLI command:

```
       aws ds register-certificate --directory-id your_directory_id --certificate-data
      file://your_file_path --type ClientCertAuth --client-cert-auth-settings
      '{"OCSPUrl":"http://your_OCSP_address"}' --region us-gov-west-1
```

For the certificate data, point to the location of your CA certificate. To provide a secondary OCSP responder address, use the optional ClientCertAuthSettings object. The response provides a certificate ID.

**Note**
 Each certificate must be registered individually.

To upload multiple certificates, the following PowerShell command can be used on Windows-based systems where the AWS CLI V2 has been installed:

```
      Get-ChildItem "C:\{file location}" -Filter *.cer | Foreach-Object { aws ds
      register-certificate --directory-id your_directory_id --certificate-data file://$_ --type
      ClientCertAuth --client-cert-auth-settings
      '{\"OCSPUrl\":\"http://{your_ocsp_address}\"}' --endpoint
      https://ds-fips.us-gov-west-1.amazonaws.com }
```

To verify the status of a CA certificate registration or a list of registered CA certificates, run the following command:

```
     aws ds list-certificates --directory-id your_directory_id
```

The following screenshot shows the successful listing of certificates registered with the specified AD Connector.

![A screenshot showing list certificates registered with AD Connector.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard16.png)

* List certificates registered with AD Connector *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
