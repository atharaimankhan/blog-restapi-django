DELIMITER //  
Create Trigger last_blog_update_trigger  
AFTER INSERT ON blogs_blog FOR EACH ROW  
    UPDATE authors_customuser
    SET last_blog_id = new.id
    WHERE id = new.author_id; //
DELIMITER ;
