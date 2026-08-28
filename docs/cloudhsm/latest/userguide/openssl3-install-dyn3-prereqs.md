---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl3-install-dyn3-prereqs.html
---

# Prerequisites for OpenSSL Dynamic Engine with AWS CloudHSM Client SDK 3
<a name="openssl3-install-dyn3-prereqs"></a>

For information about platform support, see [AWS CloudHSM Client SDK 3 supported platforms](sdk3-support.md).

Before you can use the AWS CloudHSM dynamic engine for OpenSSL with Client SDK 3, you need the AWS CloudHSM client.

The client is a daemon that establishes end-to-end encrypted communication with the HSMs in your cluster, and the OpenSSL engine communicates locally with the client. To install and configure the AWS CloudHSM client, see [Install the client (Linux)](cmu-install-and-configure-client-linux.md). Then use the following command to start it.

------
#### [ Amazon Linux ]

```
$ sudo start cloudhsm-client
```

------
#### [ Amazon Linux 2 ]

```
$ sudo systemctl start cloudhsm-client
```

------
#### [ CentOS 6 ]

```
$ sudo systemctl start cloudhsm-client
```

------
#### [ CentOS 7 ]

```
$ sudo systemctl start cloudhsm-client
```

------
#### [ RHEL 6 ]

```
$ sudo systemctl start cloudhsm-client
```

------
#### [ RHEL 7 ]

```
$ sudo systemctl start cloudhsm-client
```

------
#### [ Ubuntu 16.04 LTS ]

```
$ sudo systemctl start cloudhsm-client
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
