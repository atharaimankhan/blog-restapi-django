DELIMITER //
CREATE PROCEDURE sp_getBlogs(IN _title varchar(250), IN _author_name varchar(150), In _publication_date date)
BEGIN
    select bb.id as blog_id, bb.title as blog_title, bb.content as blog_content, group_concat(bt.name) as tags, bb.published_at as blog_published_at, author.email as author_email, concat(author.first_name, ' ' , author.last_name) as author_name from blogs_blog bb
    join authors_customuser author on author.id = bb.author_id
    left join blogs_blog_tags bbt on bbt.blog_id = bb.id
    left join blogs_tag bt on bt.id = bbt.tag_id
    where (
        _title is null or
        title like CONCAT('%', _title , '%')
    )
    and (
        _author_name is null or
        concat(author.first_name, ' ', author.last_name) like CONCAT('%', _author_name , '%')
    )
    and 
    (_publication_date is null or
     date(bb.published_at) = date(_publication_date))
    group by bb.id, author.id;
END //
DELIMITER ;