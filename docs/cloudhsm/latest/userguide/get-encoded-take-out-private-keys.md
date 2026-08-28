---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/get-encoded-take-out-private-keys.html
---

# Allow the JCE provider to extract private key secrets out of AWS CloudHSM
<a name="get-encoded-take-out-private-keys"></a>

Use the following steps to allow AWS CloudHSM JCE provider to extract your private key secrets.

**Important**
This configuration change allows extraction of all `EXTRACTABLE` key bytes in clear from your HSM cluster. For better security, you should consider using [key wrapping methods](java-lib-supported_5.md) to extract the key out of the HSM securely. This prevents unintentional extraction of your key bytes from the HSM.

1. Use the following commands to enable your **private** or **secret** keys to be extracted in JCE:

------
#### [ Linux ]

   ```
   $ /opt/cloudhsm/bin/configure-jce --enable-clear-key-extraction-in-software
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --enable-clear-key-extraction-in-software
   ```

------

1. Once you enable your clear key extraction, the following methods are enabled for extracting private keys into memory.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/cloudhsm/latest/userguide/get-encoded-take-out-private-keys.html)

If you want restore the default behavior and not allow JCE to export keys in clear, run the following command:

------
#### [ Linux ]

```
$ /opt/cloudhsm/bin/configure-jce --disable-clear-key-extraction-in-software
```

------
#### [ Windows ]

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-jce.exe" --disable-clear-key-extraction-in-software
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
