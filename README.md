# Maternity FHIR user cases
Maternity FHIR message for use case in NHS Hackathon 12/13 July 2021

Just an initial block of stub code to load up some example maternity message into FHIR bundles and return them as JSON.

There is a small piece of python code that takes a csv based on the Wessex extended data set and converts that to FHIR that will get through a LenientHandler import ,  this is a first draft.

The intention is to construct these messages from background maternity systems and then load them into kafka queues.

Details 
https://nhsconnect.github.io/FHIR-Maternity-Record/explore_plan_and_requested_actions.html

https://nhsconnect.github.io/Digital-Child-Health-STU3/explore_birth_details.html
