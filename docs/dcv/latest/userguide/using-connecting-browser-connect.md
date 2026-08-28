---
source_url: https://docs.aws.amazon.com/dcv/latest/userguide/using-connecting-browser-connect.html
---

# Connecting to a Amazon DCV session using the web browser client
<a name="using-connecting-browser-connect"></a>

The steps for connecting to a Amazon DCV session are the same across all supported web browsers. The client connects to the Amazon DCV server using your web browser's proxy settings. To connect using different proxy settings, see the documentation for your specific web browser.

**Note**
The web browser client doesn't support the QUIC (UDP) transport protocol.

**To connect to your Amazon DCV session using the web browser client**

1. Open a web browser and enter the Amazon DCV server URL in the following format:

   ```
   https://{{server_hostname_or_IP}}:{{port}}/#{{session_id}}
   ```

   In the following example, the URL connects to a session that's named `my-session`. This session is hosted on a Amazon DCV server with the hostname `my-dcv-server.com`. It's connected over port `8443`.

   ```
   https://my-dcv-server.com:8443/#my-session
   ```

1. Enter your sign-in credentials and choose **Login**.
**Note**
By default, the connection is terminated after three unsuccessful login attempts. To try again, restart the connection.

1. Your web browser might warn you that the server's certificate isn't trusted. If you're unsure about the authenticity of the certificate, confirm it with your Amazon DCV administrator. Proceed if it's safe to do so.
**Note**
This step varies depending on the web browser that you're using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
