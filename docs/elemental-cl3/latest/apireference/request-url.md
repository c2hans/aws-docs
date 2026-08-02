---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/request-url.html
---

# Request URLs
<a name="request-url"></a>

The request consists of the operation, the IP address of the Conductor Live node, and resources in a parent/child structure. For example:

```
POST http://198.51.100.0/redundancy_groups/3/members
```

In this example, the URL refers to members of the third redundancy group. That is, “redundancy groups” is the parent of each redundancy group, “3” is the ID of a particular redundancy group. The redundancy group “3” is the parent of “members”, which is the group of all members of the redundancy group 3. This POST command would contain an xml body as a child of “members” that would represent a particular member of this group.

## Specifying Pagination of the Response
<a name="specify-pagination-of-response"></a>

For responses that include large amounts of data, use pagination in the request. When you do so, your data is returned grouped into “pages” with the specified number of elements per page.

To use pagination, append your request with “?page=*x*&per\_page=*y*”, where *x* is the number of the page you want to see and *y* is the number of items shown per page. For example:

```
GET http://198.51.100.0/channels?page=2&per_page=15
```

will return page 2 of the list of channels presented at 15 channels per page. In this example, 198.51.100.0 is the IP address of the Conductor Live system that is managing the channels.

If you include just “page”, the system will use the default of 20 items per page. If you include just “per\_page”, the system with use the default of 1 for page. If you do not include either, the system will return all available items at once.

**Note**
Data returned is not necessarily ordered chronologically. Therefore, do not use pagination as a filter to locate recent data.
