---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/cross-interactivity.html
---

# Cross-interactivity using events

In some scenarios, multiple micro-frontends might need to interact with each other to react to state changes or user actions. For example, multiple micro-frontends on the page can include collapsible menus. A menu appears when the user chooses a button. The menu closes when the user clicks anywhere else, including another menu that a different micro-frontend renders.

Technically, multiple micro-frontends can use a shared state library such as Redux, and a shell can coordinate it. However, that approach creates significant coupling between applications, makes code harder to test, and might slow performance during rendering.

One common, effective approach is to develop an event bus that you distribute as a library, the application shell orchestrates, and multiple micro-frontends use. In this way, each micro-frontend publishes and listens to particular events asynchronously, basing its behavior on its own internal state only. Then, multiple teams can maintain a shared wiki page that describes events and documents behaviors that user experience designers have agreed on.

In an implementation of the event-bus example, a dropdown component uses the shared bus to publish an event called `drop-down-open-menu` with a payload of `{"id": "homepage-aboutus-button"}`. The component adds a listener to the `drop-down-open-menu` event to ensure that if the bus publishes an event for a new ID, the dropdown component hides its collapsible section. In this way, the micro-frontend can react to changes asynchronously with increased performance and better encapsulation, making it easier for multiple teams to design and test behaviors.

We recommend using standard APIs implemented natively by modern browsers to improve simplicity and maintainability. The [MDN Event reference](https://developer.mozilla.org/en-US/docs/Web/Events) provides information about using events with client-side rendered applications.
