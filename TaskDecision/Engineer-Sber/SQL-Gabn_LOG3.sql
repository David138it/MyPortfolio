create table DE13MA.GABN_LOG as (
	select 
		to_date (substring (dl.data from '\d{8}'), 'YYYYMMDD') as DT,
		cast (split_part (substring (replace (substring (dl.data, strpos (dl.data, 'http://')), chr(9), '+'), 1, strpos (replace (substring (dl.data, strpos(dl.data, 'http://')), chr(9), '|'), '/5.0') -1), '+', 1) as VARCHAR(50)) LINK,
		cast (split_part (replace (substring (dl.data from 1), chr(9), '+'), '+', 8 ) as VARCHAR(200)) USER_AGENT,
		cast (split_part (di.data, chr(9), 2) as VARCHAR(30)) REGION
	from de.log as dl
	left join de.ip as di
	on
		substring (dl.data, 1, strpos (dl.data, chr(9))) = 
			substring (di.data, 1, strpos (di.data, chr(9))));
select * from DE13MA.GABN_LOG;
