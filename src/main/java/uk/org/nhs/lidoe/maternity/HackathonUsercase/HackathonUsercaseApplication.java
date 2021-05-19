package uk.org.nhs.lidoe.maternity.HackathonUsercase;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;

import java.lang.reflect.GenericSignatureFormatError;

import org.springframework.beans.factory.annotation.Value;

@SpringBootApplication
public class HackathonUsercaseApplication {



	public static void main(String[] args) {
		SpringApplication.run(HackathonUsercaseApplication.class, args);

	
		
	}

	// public String getMaternity() {
	// 	MaternityFHIRBundle mfhirTest = new MaternityFHIRBundle(rMatJSON,false);
	// 	return mfhirTest.toString();
	// }


}
