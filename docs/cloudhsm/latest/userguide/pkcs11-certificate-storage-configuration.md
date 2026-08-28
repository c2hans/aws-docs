---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-configuration.html
---

# Enabling certificate storage
<a name="pkcs11-certificate-storage-configuration"></a>

 You can enable certificate storage on hsm2m.medium clusters using the PKCS \#11 library configuration tool. This feature is available in SDK versions 5.13 and later. For a list of operations that support the certificate object type, see [Certificate storage API operations](pkcs11-certificate-storage-api.md).

 To enable certificate storage, follow these steps for your operating system:

------
#### [ Linux ]
+

****Enable certificate storage****
Run the following command:

  ```
  $ sudo /opt/cloudhsm/bin/configure-pkcs11 --enable-certificate-storage
  ```

------
#### [ Windows ]
+

****Enable certificate storage****
Open a command prompt and run the following command:

  ```
  PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-pkcs11.exe" --enable-certificate-storage
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
