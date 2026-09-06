---
source_url: https://docs.aws.amazon.com/dcv/latest/gw-admin/manage-start.html
---

# Starting the Connection Gateway
<a name="manage-start"></a>

Manually start the Connection Gateway service using the command line.

**To start the Connection Gateway service**
Use the following command:

```
$ sudo systemctl start dcv-connection-gateway
```

Configure the Connection Gateway service to start automatically.

**To configure the Connection Gateway service to start automatically**
Use the following command:

```
$ sudo systemctl enable dcv-connection-gateway
```
