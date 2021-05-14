package uk.org.nhs.lidoe.maternity.HackathonUsercase;

import org.hl7.fhir.dstu3.model.Bundle;
import org.hl7.fhir.dstu3.model.Parameters.ParametersParameterComponent;

import ca.uhn.fhir.context.FhirContext;

// Imports for reading in JSOn from resources.
import org.springframework.core.io.Resource;

public class MaternityFHIRBundle {


    Bundle  bMaternity;
    FhirContext ctx;

    public MaternityFHIRBundle(Resource res) {
       //System.out.println(res.toString());
       ResourceFile rf =  new ResourceFile(res);

       ctx = FhirContext.forDstu3();

       bMaternity = ctx.newXmlParser().parseResource(Bundle.class,rf.toString());

    }

    public String toString() {
       return toJSON();
    }

    public String toXML() {
        return ctx.newXmlParser().encodeResourceToString(bMaternity);
    }

    public String toJSON() {
        return ctx.newJsonParser().encodeResourceToString(bMaternity);
    }
    
}
