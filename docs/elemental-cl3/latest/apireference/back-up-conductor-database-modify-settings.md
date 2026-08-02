---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/back-up-conductor-database-modify-settings.html
---

# PUT: Modify Database Backup Settings
<a name="back-up-conductor-database-modify-settings"></a>

You can view and modify the current backup settings for the conductor database on the web UI at Settings>Backups. The following command allows you to modify these settings via REST.

## HTTP Request and Response
<a name="back-up-conductor-database-modify-settings-http-request-response"></a>

### Request URL
<a name="back-up-conductor-database-modify-settings-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/cluster/backups
```

### Call Header
<a name="back-up-conductor-database-modify-settings-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="back-up-conductor-database-modify-settings-http-request-response-request-body"></a>

The response contains XML content consisting of one `backup` element with the following elements.

| Element | Value | Description |
| --- | --- | --- |
| database\_backup\_dir | string | The directory where backup files are stored. Default: /home/elemental/database\_backups |
| database\_backup\_count | integer | The number of backups stored in the system. Default: 5 |
| database\_backup\_minutes | integer | The time , in minutes, between automatic backups. Default: 1440 |

## Example
<a name="back-up-conductor-database-modify-settings-example"></a>

This request changes the backup directory to /home/elemental/database\_backups, sets the system to retain the 6 most recent backups and sets the time between backups to three hours.

```
PUT http://198.51.100.0/cluster/backups
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<backup>
  <database_backup_dir>/home/elemental/database_backups2</database_backup_dir>
  <database_backup_count>6</database_backup_ count>
  <database_backup_minutes>180</database_backup_minutes>
</backup>
```
