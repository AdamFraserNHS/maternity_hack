package uk.org.nhs.lidoe.maternity.HackathonUsercase;

import java.nio.file.Files;
import java.io.IOException;
import java.io.File;

import org.springframework.core.io.Resource;

public class ResourceFile {

    private String rfString;

    public ResourceFile( Resource resource ) {

        try {
			File file = resource.getFile();
			rfString =  new String( Files.readAllBytes(file.toPath()));		
		} catch( IOException e){
			e.printStackTrace();
		}
    }
    
    public String toString() {
        return rfString;
    }
}
