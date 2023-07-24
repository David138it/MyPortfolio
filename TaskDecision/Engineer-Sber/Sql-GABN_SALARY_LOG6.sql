/*create table de13ma.gabn_SALARY_HIST as (
	select 
		PERSON,
		CLASS,
		SALARY,
		dt as effective_from,
		coalesce((
			lead(dt) 
			over (
				partition by person 
				order by dt) - interval '1 day')::date,  
			to_date('9999-12-31', 'YYYY-MM-DD')) as effective_to
	from de.HISTGROUP);*/
--select * from de13ma.gabn_SALARY_HIST;
--select * from de.SALARY_PAYMENTS;
/*create table de13ma.gabn_SALARY_LOG as (
	select --*--,
		dgsh.person as PERSON,
		dsp.dt as PAYMENT_DT,
		dsp.payment as PAYMENT,
		--sum(dsp2.payment) as MONTH_PAID,
		--sum(dsp.payment) over (order by dsp.dt between dgsh.effective_from and dgsh.effective_to) as MONTH_PAID,
		sum(dsp.payment) over (partition by dsp.payment order by dsp.dt) as MONTH_PAID,
		dgsh.salary-sum(dsp.payment) as MONTH_REST--,
		--dgsh.salary
	from de13ma.GABN_SALARY_HIST as dgsh
	inner join de.SALARY_PAYMENTS as dsp 
		on dgsh.person=dsp.person 
	--inner join de.SALARY_PAYMENTS as dsp2 
	--	on dsp.dt >= dsp2.dt
	where dsp.dt between dgsh.effective_from and dgsh.effective_to
	group by dgsh.person,
		dsp.dt,
		dsp.payment,
		dgsh.salary--,
		--dgsh.effective_from,
		--dgsh.effective_to
	order by dgsh.person,
		dsp.dt);*/
select * from de13ma.gabn_SALARY_LOG;