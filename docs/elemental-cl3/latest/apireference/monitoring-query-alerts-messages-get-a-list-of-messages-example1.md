---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example1.html
---

# Example 1
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-example1"></a>

This example requests all active messages for node 2.

```
GET http://10.4.138.230/messages?node=2&status=active
---------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<messages href="/messages" product="AWS Elemental Conductor Live" version="3.3.nnnnn" type="array">
<messages>
  <message>
    <id type="integer">5</id>
    <type>AuditMessage</type>
    <code type="integer">30</code>
    <message>Node live_1 activated</message>
    <data nil="true"/>
    <notes nil="true"/>
    <messageable_type>Elemental::Live247::Node</messageable_type>
    <messageable_id type="integer">2</messageable_id>
    <remote_id type="integer">280</remote_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-04-28T09:40:18-07:00</updated_at>
    <readable_type>Node</readable_type>
    <ignore type="boolean">false</ignore>
  </message>
  <message>
    <id type="integer">6</id>
    <type>AuditMessage</type>
    <code type="integer">32</code>
    <message>Node live_1 added to cluster</message>
    <data nil="true"/>
    <notes nil="true"/>
    <messageable_type>Elemental::Live247::Node</messageable_type>
    <messageable_id type="integer">2</messageable_id>
    <remote_id type="integer">279</remote_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-04-28T09:38:03-07:00</updated_at>
    <readable_type>Node</readable_type>
    <ignore type="boolean">false</ignore>
  </message>
  <message>
    <id type="integer">7</id>
    <type>AuditMessage</type>
    <code type="integer">31</code>
    <message>Node live_1 is deactivated</message>
    <data nil="true"/>
    <notes nil="true"/>
    <messageable_type>Elemental::Live247::Node</messageable_type>
    <messageable_id type="integer">2</messageable_id>
    <remote_id type="integer">278</remote_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-04-28T09:17:13-07:00</updated_at>
    <readable_type>Node</readable_type>
    <ignore type="boolean">false</ignore>
  </message>
  <message>
    <id type="integer">8</id>
    <type>AuditMessage</type>
    <code type="integer">30</code>
    <message>Node live_1 activated</message>
    <data nil="true"/>
    <notes nil="true"/>
    <messageable_type>Elemental::Live247::Node</messageable_type>
    <messageable_id type="integer">2</messageable_id>
    <remote_id type="integer">86</remote_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-02-15T15:52:53-08:00</updated_at>
    <readable_type>Node</readable_type>
    <ignore type="boolean">false</ignore>
  </message>
  </messages>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
