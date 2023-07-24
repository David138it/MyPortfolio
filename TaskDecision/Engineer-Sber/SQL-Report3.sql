create table DE13MA.GABN_LOG_REPORT as (SELECT
		region, 
		browser--, 
		--cnt
	FROM (select
		t1.* , 
		ROW_NUMBER() OVER (PARTITION BY region ORDER BY cnt DESC) as numb
	FROM (select 
			cast (split_part (di.data, chr(9), 2) as VARCHAR(30)) REGION, 
			cast (split_part (substring (replace (substring (dl.data, strpos(dl.data, 'http://')), chr(9), '+'), 1, strpos (replace (substring (dl.data, strpos (dl.data, 'http://')), chr(9), '|'), '/5.0') -1), '+', 4) as VARCHAR(10)) BROWSER,
			count(1) as cnt
		from de.log as dl
		--order by dl.data
		left join de.ip as di
		--on dl.data=di.data;
		on 
			substring (dl.data, 1, strpos (dl.data, chr(9))) =
				substring (di.data, 1, strpos (di.data, chr(9)))	
		--order by region
		group by region, browser) 
		as t1)
	as t2
	WHERE numb = 1);
select * from DE13MA.GABN_LOG_REPORT;