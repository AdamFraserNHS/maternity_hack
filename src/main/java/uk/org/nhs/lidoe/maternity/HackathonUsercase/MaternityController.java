package uk.org.nhs.lidoe.maternity.HackathonUsercase;


import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.MediaType;

import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.beans.factory.annotation.Value;

@RestController
public class MaternityController {


    @Value("classpath:pregnancy_episode.xml")
	private Resource rPregFHIR;
    @Value("classpath:pregnancy_outcome_example.xml")
	private Resource rPregOutFHIR;
	@Value("classpath:birth_event.xml")
	private Resource rBirthFHIR;
	@Value("classpath:maternity.json")
	private Resource rMatJSON;


	@GetMapping(path="/mat",
            produces = {MediaType.APPLICATION_JSON_VALUE} )
	public String greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
		MaternityFHIRBundle mfhirTest = new MaternityFHIRBundle(rBirthFHIR,true);

        return mfhirTest.toString();
	}
}

