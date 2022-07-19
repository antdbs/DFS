from decoder import decode

tab = ['kxwf|Aye|mCK|@[vCfNj@b@S^Qj@u@n@_BvBgVrAwOdW|FmUjiAw@fE_@vBaDfQiXlvAe@fCsBbAsE`CkO|H}Av@gCnL_GlPcKzWUn@oCzHo@lHGhAObDSbF{Cp{@_AlQkAtJo@`EaBpIe@dCc@zB_I|]UzCKpCBxB`@dDh@`Cf@zAp@lAtAfBlB`B~DjDjR~LuApC{OjWqBnCxAlArXzS|B`B`BnAvJfGvDdErAdB^l@~@~A~@vBp@nBvcAhiB~@|AzF~Ib^dp@n@jApCvAzCxAtDhB~BpEjBrDd]lq@xAjCzGzLhHtRlAtExBpHl@xBlAdFVxEp@~Lb@jF`B|NbBtNlMvdAX`CzGdl@vAdM~@|Hx@zGtHpm@`AbIlOppAhA|IdFxa@hB|MpBfOfA`Jr@bGzQjyAZtDlCdZlLv`AhCrWpA`VlDgDjAiAlBeBt@q@hQ_P|@bCrI~UfBlFv[x|@hA~CvAtDpYrv@dD|IbDtIlUrm@t@rBhYxu@t@nBpr@jjBZv@pEtLf@rGDj@|AfArI~Sdf@~nAtM|^hDzJzBfDjk@`{@|^fj@xGxJpIO^vOZjNvCnExEvH|AtCnBhDvn@ngArOhXfAlBvJbQzMvUhB~Cxw@dtA|ChFpDzFoCzLtFAzEMxDKnL]', 
'kxwf|Aye|mCK|@[vCfNj@b@S^Qj@u@n@_BvBgVrAwOdW|F`WpGdt@dP~GjEhAe@b[sMhCgAlBSrKkApAO``@gExAOk@gFfA_@^Kx@YpDoAv@W`@OjAa@v@hHj@tFzGbm@xAy@zKuDjCSnY`NfEpBjAd@bFvB~LnEjC~@lCtUr@vB~@jCnEyBfFcBzBu@x@[~Cs@b@Nf@PzTlHfC|@hF~A|UbJzA`@bCp@fDbAxErArIbBlATlZ`GxAV~WbF~GnAxB`@`]tGdB^lVlEvF`BhB_Hd@aBd@_CnCsD`@c@nM_PhMsMnDmEhEwEjCwB~CiC~c@e`@~@s@zAiAdCiBfBcBpI{J`BaCtf@mu@rDwF|BcC|EmF~@cAbEgEjKsK~@g@vFaBzJ}BnFkAtAY`Di@pAQzLeArCWvRcB~FShIh@~WfDxFp@rFrAxA`@n[fHlCl@bG|ArJxB|IhBbCk@~Ci@rF{@jE{AhFmBfBaAjb@_P`Bk@vJ{DdJ}CxCaAxC_AnAa@xHcCxHcCdEmApFiBv@Up@SdLmDfM}DxHaCnC{@xCb@rANvZhDvDpA|Al@x@\\br@dZvAj@xJ|D']

result = []

for e in tab:
    result.append(decode(e))

print(result)