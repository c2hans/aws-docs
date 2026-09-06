---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/back-up-conductor-database-backup-now.html
---

# POST: Backup Database Now
<a name="back-up-conductor-database-backup-now"></a>

To initiate an immediate database backup, send the following command.

## HTTP Request and Response
<a name="back-up-conductor-database-backup-now-http-request-response"></a>

### Request URL
<a name="back-up-conductor-database-backup-now-http-request-response-url"></a>

```
POST http://<Conductor IP address>/cluster/backups
```

### Call Header
<a name="back-up-conductor-database-backup-now-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="back-up-conductor-database-backup-now-http-request-response-request-body"></a>

There is no body in the backups command.
