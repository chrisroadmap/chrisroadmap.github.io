---
layout: page
permalink: /contact/
title: contact
description: send me a message
nav: true
nav_order: 8
---

Fancy a chat? [Feel free to browse my Outlook calendar](https://outlook.office365.com/calendar/published/81009e63e9d54cbeadc90ed1d0a588be@vub.be/ca17a3550341423cad91d1d79795d2802529308089475844290/calendar.html) to find a time that I'm free.

<section class="contact-section">
    
    <form class="contact-form" action="https://api.web3forms.com/submit" method="POST">
    
        <input type="hidden" name="access_key" value="9b31ba82-9fc4-46a7-b3c7-9e886e15f15e" />
        <input type="hidden" name="subject" value="New Contact Form Submission from Web3Forms" />
        <input type="hidden" name="from_name" value="My Website" />
        <!-- More custom ization options available in the docs: https://docs.web3forms.com -->
    
        <div class="form-group-container">
        <div class="form-group">
            <label for="name" class="form-label">Name</label>
            <input id="name" name="name" class="form-input" placeholder="Your name" type="text" />
        </div>
        <div class="form-group">
            <label for="email" class="form-label">Email</label>
            <input id="email" name="email" class="form-input" placeholder="Your email" type="email" />
        </div>
        <div class="form-group">
            <label for="message" class="form-label">Message</label>
            <textarea class="form-textarea" id="message" name="message" placeholder="Your message"></textarea>
        </div>
        </div>
        <button class="form-submit" type="submit">Send Message</button>
    </form>
    
</section>