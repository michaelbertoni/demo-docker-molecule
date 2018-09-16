package com.michael.demo;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloWorldResource {

    @RequestMapping("/")
    public String index() {
        return "En voilà une application Spring Boot qu'elle est belle !";
    }

}