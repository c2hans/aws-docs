---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/setup-jupyter-start-server.html
---

# Starting the Jupyter Notebook server on a DLAMI instance
<a name="setup-jupyter-start-server"></a>

After you [secure your Jupyter Notebook server with a password and SSL](setup-jupyter-secure.md), you can start the server. Log in to your DLAMI instance and run the following command that uses the SSL certificate that you created previously.

```
$ jupyter notebook --certfile=~/ssl/mycert.pem --keyfile ~/ssl/mykey.key
```

With the server started, you can now connect to it via an SSH tunnel from your client computer. When the server runs, you will see some output from Jupyter confirming that the server is running. At this point, ignore the callout that you can access the server via a local host URL, because that won't work until you create the tunnel.

**Note**
Jupyter will handle switching environments for you when you switch frameworks using the Jupyter web interface. For more information, see [Switching Environments with Jupyter](tutorial-jupyter.md#tutorial-jupyter-switching).

**Next step**
[Connecting a client to the Jupyter Notebook server on a DLAMI instance](setup-jupyter-connect.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
